from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import ProductDetails
from .serializers import ProductDetailsSerializer

# Create your views here.
class ProductDetailsView(viewsets.ModelViewSet):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly