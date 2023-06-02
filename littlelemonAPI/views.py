from rest_framework import generics, status
from rest_framework.response import Response
from .models import MenuItem, Category
from .serializers import MenuItemiSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view




class CategoryView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = Category

# function based
@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        serialized_item = MenuItemiSerializer(items, many=True)
        return Response(serialized_item.data)
    if request.method == 'POST':
        serialized_item = MenuItemiSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_202_CREATED)

@api_view()
def sengle_item(request, pk):
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