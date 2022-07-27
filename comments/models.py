from django.db import models

from products.models import Product, User


class ProductComment(models.Model):
    '''Comment on the Products, created by customer'''
    text = models.TextField(
        blank=False,
        max_length=500,
        verbose_name='Text'
    )
    product = models.ForeignKey(
        Product,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Associated product'
    )
    customer = models.ForeignKey(
        User,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Associated user'
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created on'
    )
