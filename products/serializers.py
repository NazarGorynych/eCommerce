from rest_framework import serializers
from .models import Product


class ProductInlineSerializer(serializers.Serializer):
    '''Serializes name and url of Product for UserSerializer'''
    name = serializers.CharField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializes Product model, excluding owner field
     from Post, Put, and Patch methods
    '''

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['owner', ]
