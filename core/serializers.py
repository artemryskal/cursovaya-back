from rest_framework import serializers
from .models import *

class ProductSerializer (serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'picture', 'name', 'price', 'rate', 'description')

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'name', 'last_name', 'phone', 'email', 'address')

class PopularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'picture', 'name', 'price', 'rate', 'description')
