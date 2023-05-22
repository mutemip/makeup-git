from rest_framework import generics
from .models import MenuItem, Category
from .serializers import MenuItemiSerializer


# handling nested fields in relationship serializer

#method 1 - create serializer and include it in related model
class CategoryView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = Category

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemiSerializer

class SingleItemModelSerializer(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemiSerializer

