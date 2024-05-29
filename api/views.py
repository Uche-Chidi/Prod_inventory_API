from django.shortcuts import render
from .serializers import ProductsSerializer, CategorySerializer
from .models import Products, Category
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.

class ProductsAddListEndpoint(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field='pk'
    permission_classes = [AllowAny]


class CategoryListEndpoint(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field='pk'
    permission_classes = [AllowAny]

class AddCategoryEndpoint(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field='pk'
    permission_classes = [AllowAny]
