from rest_framework import viewsets
from .serializers import *
from .models import *

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class RequestViewSet(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

class PopularViewSet(viewsets.ModelViewSet):
    serializer_class = PopularSerializer
    queryset = Product.objects.all()[:6]
