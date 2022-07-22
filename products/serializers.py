from rest_framework import serializers
from .models import Product


class ProductInlineSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
