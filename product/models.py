from django.db import models


class Category(models.Model):
    slug = models.SlugField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

# название (char), описание (text), цена (price), category(FK).
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    description = models.TextField(max_length=255, verbose_name='Описание')
    price = models.FloatField(max_length=50, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'