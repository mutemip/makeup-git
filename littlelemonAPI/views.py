from rest_framework import generics, status
from rest_framework.response import Response
from .models import MenuItem, Category
from .serializers import MenuItemiSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
# for pagenation
from django.core.paginator import Paginator, EmptyPage

# for throttling
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import TenCallsPerMinute

#CBV
from rest_framework import viewsets

# securing API endpoint
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, throttle_classes




class CategoryView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = Category

# function based
@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        # filter per field
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        # search filter
        search = request.query_params.get('search')

        # ordering filter
        ordering = request.query_params.get('ordering')

        # for pagenation filter
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)
        
        #filtering items 
        """
        127.0.0.1:8000/api/menu-item1?category_name=beverages
        """
        if category_name:
            items = items.filter(category__title=category_name)
        """
        127.0.0.1:8000/api/menu-item1?to_price=120
        """
        if to_price:
            items = items.filter(price=to_price)
        """
        127.0.0.1:8000/api/menu-item1?search=tilapia
        """
        if search:
            items = items.filter(title__icontains=search)
        """
        127.0.0.1:8000/api/menu-item1?order_by=category
        """
        if ordering:
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)
        
        # initiating paginator object
        paginator = Paginator(items, per_page=perpage)
        """
        Try these:
        127.0.0.1:8000/api/menu-item1
        127.0.0.1:8000/api/menu-item1?perpage=3&page=1
        """
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []

        serialized_item = MenuItemiSerializer(items, many=True)
        return Response(serialized_item.data)
    if request.method == 'POST':
        serialized_item = MenuItemiSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.validated_data, status.HTTP_201_CREATED)

@api_view()
def single_item(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    serialized_item = MenuItemiSerializer(item)
    return Response(serialized_item.data)

# class based
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemiSerializer

    

class SingleItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemiSerializer

@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data)


#CBV using viewsets
class MenuItemViewSet(viewsets.ModelViewSet):
    # throttling in CBV
    throttle_classes = [AnonRateThrottle, TenCallsPerMinute] # Or -> UserRateThrottle
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemiSerializer
    # ordering & sorting
    ordering_fields = ['price', 'inventory']
    # search
    """
    Searching Nested fields
    RelatedModelName__FieldName - model=category, field=title
    category__title
    """
    search_fields = ['title', 'category__title'] 



# testing 
@api_view()
@permission_classes([IsAuthenticated])
def secret_view(request):
    return Response({"message": "some secret message"})


# testing on managing user groups 
# adding authorization layer of security via user roles
@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name="manager").exists():
        return Response({"message":"Only managers can see this!!"})
    else:
        return Response({"message":"You are not authorized!!"}, 403)

# for anonymous users
@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message":"throttling test!"})


# for authenticated users
@api_view()
@permission_classes([IsAuthenticated])
# @throttle_classes([UserRateThrottle])
@throttle_classes([TenCallsPerMinute]) # using custome throttling
def throttle_user(request):
    return Response({"message":"Only for authenticated users!!"})
"""
NB:
caching: a technique of serving saved results instaed of creating new one whenver it's requested
    - reduces the server load &
    - Bandwidth consumption
caching can be split in multiple layers
can be done on:
    - reverse proxy
    - web server 
    - database server

1. Caching on database layer: done to prevent excessive read-write operation in the storage
 - Uses Query cache - where SQL query & query results are stored in memory.
 If no change of data, the stored data will be served whenever a request is made, saving processing power and time.

2. Caching on web server: runs server side scripts which can cache data if it's certain that there was no changes on it.
It caches data in a simple files or databases or caching tools like redis, Memcached etc - which can save database connections everytime.
Server-side scripts cache response results in a separate cache storage, which could be simple files, or a database, or in caching tools.

3. Reverse Proxy: used by trafic heavy applications on top of other servers to distribute the requests evenly.
The reverse proxy server caches response results for a certain amount of time in caching headers received from the web server.

4. Client cache: Reverse proxies or web servers can send responses with caching headers, which tell the client to cache the request for a specific time.
"""

"""
Token Based Authentication

- Users send their username and password once->
if cridentials are correct, A unique token is generated on the server. 
- When client makes a new API request, the token is included 
- server side scripts checks whether its valid or expired.
- if valid, it matches the user with respective user.

- The token is validated with help of TokenAuthentication class in auth token App in the DRF

This process helps avoid sending username and password in every request.
"""

"""
Throttling / rate limiting

Helps to limit amount of time an API can be accessed in given time.
2 Types of throttling:
    - Anonymous Throttling for unauthenticated users -> used when there is no token on the API header.
    - User Throttling for authenticated users -> Used when there are valid tokens


"""

    