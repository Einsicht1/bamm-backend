from django.db import models
from django.utils import timezone

from core.models import BaseModel
from products.models import Product
from users.models import User


class Order(BaseModel):
    class Status(models.Choices):
        PAYMENT_PENDING = "결제 대기"
        PAYMENT_COMPLETED = "결제 완료"
        SHIPPING_PENDING = "배송 대기"
        SHIPPING_IN_PROGRESS = "배송 중"
        SHIPPING_COMPLETED = "배송 완료"
        PURCHASE_CONFIRMED = "구매 확정"

    user = models.ForeignKey(
        User, verbose_name="유저", blank=True, null=True, on_delete=models.DO_NOTHING
    )
    order_id = models.CharField(unique=True, max_length=200, verbose_name="주문번호")
    product = models.ForeignKey(Product, verbose_name="상품", on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=1, verbose_name="수량")
    total_amount = models.DecimalField(
        max_digits=13, decimal_places=2, verbose_name="결제 금액"
    )
    status = models.CharField(
        choices=Status.choices,
        default=Status.PAYMENT_PENDING,
        verbose_name="주문 상태",
        max_length=50,
    )

    class Meta:
        db_table = "orders"
        verbose_name = "주문"
        verbose_name_plural = "주문"

    def delete(self, using=None, keep_parents=False):
        self.soft_delete()

    @classmethod
    def generate_order_id(cls):
        today = timezone.now().strftime("%Y%m%d")
        last_order = (
            cls.objects.filter(order_id__startswith=today).order_by("-order_id").first()
        )
        if last_order:
            last_order_id = last_order.order_id.split("-")[-1]
            new_order_id = f"{today}-{int(last_order_id) + 1:06}"
        else:
            new_order_id = f"{today}-000001"
        return new_order_id

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = self.generate_order_id()
        super().save(*args, **kwargs)
