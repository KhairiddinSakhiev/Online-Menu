from rest_framework import serializers

from .models import Product, Menu, Category



class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'image', 'status']

    def get_title(self, obj):
        return {
            'en': obj.title_en,
            'ru': obj.title_ru,
            'tj': obj.title_tj
        }
    
    def get_description(self, obj):
        return {
            'en': obj.description_en,
            'ru': obj.description_ru,
            'tj': obj.description_tj
        }


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'description', 'image', 'availability_status']

    def get_title(self, obj):
        return {
            'en': obj.title_en,
            'ru': obj.title_ru,
            'tj': obj.title_tj
        }
    
    def get_description(self, obj):
        return {
            'en': obj.description_en,
            'ru': obj.description_ru,
            'tj': obj.description_tj
        }


class CategoryWithProductsSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True, source='product_set')
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'image', 'status', 'products']
    
    def get_title(self, obj):
        return {
            'en': obj.title_en,
            'ru': obj.title_ru,
            'tj': obj.title_tj
        }
    
    def get_description(self, obj):
        return {
            'en': obj.description_en,
            'ru': obj.description_ru,
            'tj': obj.description_tj
        }


class MenuWithCategoriesSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True, source='category_set')

    class Meta:
        model = Menu
        fields = ['id', 'title', 'description', 'status', 'category']


