from rest_framework import viewsets
from rest_framework.decorators import action

from products.models import Product, User
from products.serializers import ProductSerializer
from users.serializers import UserPublicSerializer
from users.services import get_current_user


class ProductViewSet(viewsets.ModelViewSet):
    '''View-set (CRUD) to retrieve and work on Products and their instances'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(owner=get_current_user())

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    View-set (GET) to retrieve User instances.
    Users can not be modified due to confidentiality
    '''
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
