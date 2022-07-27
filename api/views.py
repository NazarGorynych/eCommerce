from rest_framework import viewsets, generics
from rest_framework.decorators import action

from comments.models import ProductComment
from comments.serializers import ProductCommentSerializer

from products.models import Product, User
from products.serializers import ProductSerializer

from users.serializers import UserPublicSerializer
from users.services import get_current_user


class ProductCommentViewSet(viewsets.ModelViewSet):
    '''View-set (CRUD) to retrieve and work on Comments and their instances'''
    serializer_class = ProductCommentSerializer
    queryset = ProductComment.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    '''View-set (CRUD) to retrieve and work on Products and their instances'''
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=get_current_user())


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    View-set (GET) to retrieve User instances.
    Users can not be modified due to confidentiality
    '''
    serializer_class = UserPublicSerializer
    queryset = User.objects.all()
