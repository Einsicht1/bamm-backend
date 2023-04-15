import requests
from django.db import transaction

from core.utils.portone import get_portone_access_token
from orders.models import Order


class OrderValidationService:
    def validate(self, **kwargs):
        imp_uid = kwargs["imp_uid"]
        merchant_uid = kwargs["merchant_uid"]
        order = self._get_order(merchant_uid)
        access_token = get_portone_access_token()

        payment_detail = self._get_payment_detail_from_portone(access_token, imp_uid)
        if payment_detail["code"] == -1:
            "존재하지 않는 결제정보입니다. 흑흑 뭐라도 조치해야 함."
        if payment_detail["code"] == 0:
            "존재하지 않는 결제정보입니다."
        if (
            payment_detail["response"]["merchant_uid"] == merchant_uid
            and payment_detail["response"]["amount"] == order.total_amount
            and payment_detail["response"]["status"] == "paid"
        ):
            with transaction.atomic:
                order.status = Order.Status.PAYMENT_COMPLETED
                order.product.is_soldout = True
                order.product.quantity -= 1
                order.save()
                order.product.save()
            print("결제 성공")
            return
        print("결제 검증 실패")

    def _get_payment_detail_from_portone(self, access_token: str, imp_uid: str):
        order_validation_url = f"https://api.iamport.kr/payments/{imp_uid}"
        headers = {"Authorization": f"Bearer {access_token}"}
        res = requests.get(order_validation_url, headers=headers)
        res_json = res.json()
        print(res_json)
        return res_json

    def _get_order(self, merchant_uid: str) -> Order | None:
        try:
            return Order.objects.get(order_id=merchant_uid)
        except Order.DoesNotExist:
            raise


order_validation_service = OrderValidationService()
