from modeltranslation.translator import register, TranslationOptions

from api.models import Menu, Category, Product


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )