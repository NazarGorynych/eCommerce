from products.models import Product, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
