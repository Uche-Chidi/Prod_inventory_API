from rest_framework import serializers
from .models import Products, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ProductsSerializer(serializers.ModelSerializer):
   category = CategorySerializer(read_only=True)
   class Meta:
       model = Products
       fields = ('id', 'name', 'brand', 'price', 'description', 'category')

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'brand', 'price', 'category', 'description')
    
