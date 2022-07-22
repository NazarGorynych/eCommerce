from rest_framework import viewsets

from products.serializers import ProductSerializer
from users.serializers import UserPublicSerializer
from products.models import Product, User


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
