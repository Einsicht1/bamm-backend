from rest_framework.generics import ListAPIView, RetrieveAPIView

from products.models import Product
from products.serializers import ProductSerializer


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()



class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
