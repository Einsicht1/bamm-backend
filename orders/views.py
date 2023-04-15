from rest_framework.generics import CreateAPIView

from orders.serializers import OrderCreateSerializer


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderCreateSerializer
