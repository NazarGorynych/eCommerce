from rest_framework import serializers

from .models import ProductComment


class ProductCommentInlineSerializer(serializers.Serializer):
    '''Serializes name and url of Product for UserSerializer'''
    url = serializers.HyperlinkedIdentityField(
        view_name='productcomment-detail',
        lookup_field='pk',
        read_only=True
    )


class ProductCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductComment
        fields = '__all__'
        read_only_fields = ['author', 'product']