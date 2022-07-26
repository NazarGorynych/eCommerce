from products.models import User, Product
from rest_framework import serializers
from products.serializers import ProductInlineSerializer


class UserPublicSerializer(serializers.HyperlinkedModelSerializer):
    '''Public serializer to limit the meta information of the user'''
    products = serializers.SerializerMethodField('get_products')

    class Meta:
        model = User
        fields = ('username', 'id', 'products',)

    def get_products(self, user):
        '''Retrieve all products of the user in list with hyperlinked urls '''
        products = Product.objects.filter(owner=user.id)
        return ProductInlineSerializer(products, many=True, context=self.context).data
