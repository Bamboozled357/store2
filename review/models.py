from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# В приложении review создать модель Review с полями author(FK) использовать встроенную модель пользователя,
# product(FK), text(Text), rating(integer от 1 до 5).
from product.models import Product


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    text = models.TextField(verbose_name='Текст')
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], verbose_name='Рейтинг')

    def __str__(self):
        return f'Автор: {self.author}, Продукт: {self.product}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'