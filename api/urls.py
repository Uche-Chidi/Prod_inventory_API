from django.urls import path
from .views import CategoryListEndpoint, AddCategoryEndpoint, ProductsAddListEndpoint

urlpatterns = [
    path('category', CategoryListEndpoint.as_view(), name='category'),
    path('add/category', AddCategoryEndpoint.as_view(), name='add-cate'),
    path('products', ProductsAddListEndpoint.as_view(), name='products'),
]