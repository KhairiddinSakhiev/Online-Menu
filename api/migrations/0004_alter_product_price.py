# Generated by Django 5.0 on 2024-11-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_category_description_en_category_description_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]