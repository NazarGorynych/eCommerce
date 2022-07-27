from rest_framework import serializers
from .models import Product

from comments.models import ProductComment
from comments.serializers import ProductCommentInlineSerializer


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
    comments = serializers.SerializerMethodField('get_comments')

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['owner', 'comments']

    def get_comments(self, product):
        comments = ProductComment.objects.filter(product=product.id)
        return ProductCommentInlineSerializer(comments, many=True, context=self.context).data
