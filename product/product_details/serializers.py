from rest_framework import serializers
from .models import ProductDetails

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = ('id', 'name', 'price', 'image_link', 'quantity')