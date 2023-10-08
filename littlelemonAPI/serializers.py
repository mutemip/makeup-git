from datetime import datetime
from rest_framework import serializers
from .models import MenuItem, Category, Rating,  Cart, Order, OrderItem
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
    
class RatingSerializer (serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
            queryset=User.objects.all(),
            default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Rating
        fields = ['user', 'menuitem_id', 'rating']

    validators = [
        UniqueTogetherValidator(
            queryset=Rating.objects.all(),
            fields=['user', 'menuitem_id']
        )
    ]

    extra_kwargs = {
        'rating': {'min_value': 0, 'max_value':5},
    }
    
class OrderSerializer(serializers.ModelSerializer):
    Date = serializers.SerializerMethodField()
    date = serializers.DateTimeField(write_only=True, default=datetime.now())
    order_items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'total', 'date', 'Date']
        extra_kwargs = {
            'total': {'read_only': True}
        }

    def get_date(self, obj):
        return obj.date.strftime('%Y-%m-%d')
    
    def get_order_items(self, obj):
        order_items = OrderItem.objects.filter