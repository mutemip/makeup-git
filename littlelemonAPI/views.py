<<<<<<< HEAD
from rest_framework import generics
from .models import MenuItem, Category
from .serializers import MenuItemiSerializer, CategorySerializer
=======
from rest_framework import generics, status
from rest_framework.response import Response
from .models import MenuItem, Category, Rating
from .serializers import MenuItemiSerializer, CategorySerializer, RatingSerializer
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
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User, Group
from rest_framework.decorators import permission_classes, throttle_classes

>>>>>>> f30adedca8198d03a249422a71d0cb87cbdf23b6



class CategoryView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = Category

<<<<<<< HEAD
class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.get(pk=pk) 
    serializer_class = CategorySerializer

=======
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
        perpage = request.query_params.get('perpage', default=5)
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
>>>>>>> f30adedca8198d03a249422a71d0cb87cbdf23b6
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemiSerializer

    ordering_fields = ['price', 'inventory']
    search_fields = ['title', 'category__title'] 
    


    

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
    # throttle_classes = [AnonRateThrottle, TenCallsPerMinute] # Or -> UserRateThrottle
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
    
    # conditional throtthling for any POST requests
    def get_throttles(self):
        if self.action == "create":
            throttle_classes = [UserRateThrottle]
        else:
            throttle_classes = []
        return [throttle() for throttle in throttle_classes]


# testing 
@api_view()
@permission_classes([IsAuthenticated])
def secret_view(request):
    return Response({"message": "some secret message"})


# testing on managing user groups 
# adding authorization layer of security via user roles
@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def manager_view(request):
    # if request.user.groups.filter(name="manager").exists():
    #     return Response({"message":"Only managers can see this!!"})
    # else:
    #     return Response({"message":"You are not authorized!!"}, 403)
    username = request.data['username']
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="manager")
        if request.method == 'POST':
            managers.user_set.add(user)
            if request.user.groups.filter(name="manager").exists():
                return Response({"message": "User Already in manager group!"})
            else:
                return Response({"message": "User Added to  manager group!"})
        elif request.method == "DELETE":
            managers.user_set.remove(user)
            return Response({"message": f"{user} removed from the manager group."})
            
        
    return Response({"message": "Error!!"}, status.HTTP_400_BAD_REQUEST)

# @api_view(['POST', 'DELETE'])
# @permission_classes([IsAuthenticated, IsAdminUser])
# def delivery_view(request):
#     username = request.data['username']
#     if username:
#         user = get_object_or_404(User, username=username)
#         deliverys = Group.objects.get(name="delivery")
#         if request.method == 'POST':
#             deliverys.user_set.add(user)
#             if request.user.groups.filter(name="delivery").exixts():
#                 return Response({"message": "User already in Delivery group!"})
#             else:
#                 return Response({"message": "User added to delivery group"})
#         elif request.method == "DELETE":
#             deliverys.user_set.remove(user)
#             return Response({"message": f"{user} removed from the delivery group"})
#     return Response({"message": "Error!!"}, status.HTTP_400_BAD_REQUEST)
@api_view()
@permission_classes([IsAuthenticated])
def me(request):
    return Response(request.user.email)

# for anonymous users
@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def throttle_check(request):
    return Response({"message":"throttling test!"})


# for authenticated users
@api_view()
@permission_classes([IsAuthenticated])
# @throttle_classes([UserRateThrottle])
@throttle_classes([TenCallsPerMinute]) # using custome throttling
def throttle_user(request):
    return Response({"message":"Only for authenticated users!!"})



class RatingsView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if(self.request.method=='GET'):
            return []

        return [IsAuthenticated()]
    