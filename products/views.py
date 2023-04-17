from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from products.models import Product
from products.renderers import NaverPayXMLRenderer
from products.serializers import NaverPayProductValidationSerializer, ProductSerializer


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("-id")


class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class NaverPayProductValidationAPIVIew(GenericAPIView):
    renderer_classes = (NaverPayXMLRenderer,)
    serializer_class = NaverPayProductValidationSerializer

    def get(self, request, *args, **kwargs):
        valid_query_params = {
            k: v for k, v in request.query_params.items() if "product" in k
        }
        ids = [v for k, v in valid_query_params.items() if "id" in k]
        product = Product.objects.filter(id__in=ids)
        serializer = self.get_serializer(product, many=True)

        return Response(serializer.data)
