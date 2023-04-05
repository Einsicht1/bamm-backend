from django.db import models

from core.models import BaseModel


class Order(BaseModel):
    number = models.UUIDField(verbose_name="")
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name="상품명")
    quantity = models.IntegerField(default=1, verbose_name="수량")
    price = models.IntegerField(verbose_name="가격")
    size = models.CharField(max_length=50, blank=True, null=True, verbose_name="크기")
    material = models.CharField(max_length=50, blank=True, null=True, verbose_name="제작방식")
    short_description = models.CharField(max_length=50, blank=True, null=True, verbose_name="작품 설명")
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING, verbose_name="작가")
    is_soldout = models.BooleanField(default=False, verbose_name="품절 여부")

    class Meta:
        db_table = "order"
        verbose_name = "주문"
        verbose_name_plural = "주문"

    def __str__(self):
        return f"{self.id}"


# Create your models here.
