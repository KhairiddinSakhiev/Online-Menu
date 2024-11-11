from rest_framework import generics
from django.db.models import Prefetch

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
    queryset = Product.objects.all().order_by('-rating')
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
    
    serializer_class = CategoryWithProductsSerializer

    def get_queryset(self):
        return Category.objects.prefetch_related(
            Prefetch('product_set', queryset=Product.objects.order_by('-rating'))
        ).all()


class RecommendedProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        # Filter products with rating > 5 and limit the results to 8
        print(len(Product.objects.order_by('-rating')[:8]))
        return Product.objects.order_by('-rating')[:8]


class MenuWithCategoriesListView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuWithCategoriesSerializer