from django.db import models


class Menu(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Menu")
        verbose_name_plural = ("Menus")

    def __str__(self):
        return self.title
    

class Category(models.Model):

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/')
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")

    def __str__(self):
        return self.title
    

class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    availability_status = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.title
    