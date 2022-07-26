from django.db import models

from users.models import User
from users.services import get_current_user


class Product(models.Model):
    ''' Product entity which user can buy or sell'''
    name = models.CharField(
        blank=False,
        max_length=60,
        verbose_name='Name')
    price = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=1000000,
        verbose_name='Price')
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Owner')
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created on')
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name='Modified on')  # automatically sets current date every time model is saved
    description = models.TextField(
        blank=True,
        verbose_name='Description')
    available = models.BooleanField(
        default=True,
        verbose_name='Available')

    # comment = models.ForeignKey(
    #     Comment,
    #     blank=True,
    #     null=True,
    #     on_delete=models.CASCADE,
    #     verbose_name='Owner'))

    def is_available(self):
        return self.available
