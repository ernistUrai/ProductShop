from rest_framework import viewsets
from rest_framework import status

from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

