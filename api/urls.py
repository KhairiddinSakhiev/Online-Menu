from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import (MenuListView, CategoryListView, 
                    ProductListView, ProductsByCategory, 
                    CategoryWithProductsListView,
                    MenuWithCategoriesListView, 
                    ProductDetailView, )



urlpatterns = [
    path('menus/', MenuListView.as_view(), name='menu_list'),
    path('menu-with-categories/', MenuWithCategoriesListView.as_view(), name='menu_with_categories'),

    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category-with-products/', CategoryWithProductsListView.as_view(), name='category_with_product'),

    path('products/', ProductListView.as_view(), name='product_list'),
    path('products-by-category/<int:category_id>/', ProductsByCategory.as_view(), name='product_by_category'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
