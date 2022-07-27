from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from products.models import Product
from users.models import User
from comments.models import ProductComment


class Admin(UserAdmin):
    model = User
    list_display = ['email', 'username', ]


admin.site.register(Product)
admin.site.register(ProductComment)