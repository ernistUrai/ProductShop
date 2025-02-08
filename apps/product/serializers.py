from rest_framework import serializers

from .models import Category, Product, Cart

class CategorySerializer(serializers.ModelSerializer):  
    class Meta:
        model = Category
        fields = ['id', 'name',  'parent', ]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'image', 'description', 'price', 'year', 'country' ]  
        
class CartSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    # product = serializers.ReadOnlyField(source='product.name')
    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'quantity', 'total_price', 'created_at', 'updated_at']