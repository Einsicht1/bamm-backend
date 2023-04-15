from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from orders.models import Order


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "product",
            "quantity",
            "total_amount",
            "user",
        ]

    def validate(self, attrs):
        product = attrs["product"]
        if product.is_soldout:
            raise ValidationError("이미 품절된 상품입니다.")
        if attrs["quantity"] > product.quantity:
            raise ValidationError("구매 가능한 수량을 초과했습니다.")
        if attrs["quantity"] < 1:
            raise ValidationError("수량은 최소 1개 이상 선택해야 합니다.")
        if attrs["total_amount"] < 0:
            raise ValidationError("결제금액은 0원 이상이어야 합니다.")

        return attrs
