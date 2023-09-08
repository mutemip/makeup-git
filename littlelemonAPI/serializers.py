from rest_framework import serializers
from .models import MenuItem, Category, Rating
from decimal import Decimal
# import bleach
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User


# handling nested fields in relationship serializer

#method 1 - create serializer and include it in related model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

# class MenuItemiSerializer(serializers.HyperlinkedModelSerializer):
class MenuItemiSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source = 'inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    # category = serializers.HyperlinkedRelatedField(
    #     queryset = Category.objects.all(),
    #     view_name= ('category-detail')
    # )
    # def validate_title(self, value):
    #         return bleach.clean(value)
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
        # method 2 - instead of creation serializer, use depth=1 in meta class and all related fields of will be desplayed
        # depth = 1

    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.16)
    
class RatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), defualt=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Rating
        fields = ['menuitem_id', 'rating']
        validators = UniqueTogetherValidator(queryset=Rating.objects.all(), fields=['user', 'menuitem_id', 'rating'])
        extra_kwargs = {
            'rating':{
                'max_value': 5, 
                'min_value': 0
            }
        }

    
