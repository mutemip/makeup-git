from rest_framework import serializers
from .models import MenuItem

class MenuItemiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']