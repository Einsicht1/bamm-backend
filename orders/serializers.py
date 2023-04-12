from rest_framework import serializers

from orders.models import Order


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "product",
            "quantity",
            "status",
            "total_amount",
            "user",
        ]
