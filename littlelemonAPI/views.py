from rest_framework import generics
from rest_framework.response import Response
from .models import MenuItem, Category
from .serializers import MenuItemiSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view




class CategoryView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = Category

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemiSerializer
    

class SingleItemModelSerializer(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemiSerializer

@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data)