from rest_framework import generics

from .models import Menu, Category, Product
from .serializers import (MenuSerializer, CategorySerializer, 
                          ProductSerializer, CategoryWithProductsSerializer,
                          MenuWithCategoriesSerializer, )



class MenuListView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    

class CategoryWithProductsListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWithProductsSerializer


class MenuWithCategoriesListView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuWithCategoriesSerializer