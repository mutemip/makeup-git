from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemiSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemiSerializer