from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal

# handling nested fields in relationship serializer

#method 1 - create serializer and include it in related model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemiSerializer(serializers.HyperlinkedModelSerializer):
    stock = serializers.IntegerField(source = 'inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = serializers.HyperlinkedRelatedField(
    #     queryset = Category.objects.all(),
    #     view_name= ('category-detail')
    # )
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']
        # method 2 - instead of creation serializer, use depth=1 in meta class and all related fields of will be desplayed
        # depth = 1

    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.16)
    
