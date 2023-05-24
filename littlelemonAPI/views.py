from rest_framework import generics
from .models import MenuItem, Category
from .serializers import MenuItemiSerializer, CategorySerializer



class CategoryView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = Category

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.get(pk=pk) 
    serializer_class = CategorySerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemiSerializer

class SingleItemModelSerializer(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemiSerializer

