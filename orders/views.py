from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from orders.serializers import OrderCreateSerializer, PortOneWebhookSerializer
from orders.services.order_validation_service import order_validation_service


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderCreateSerializer


class PortOneWebhookAPIView(GenericAPIView):
    serializer_class = PortOneWebhookSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_validation_service.validate(**serializer.validated_data)
        return Response()
