from django.db import models

from artists.models import Artist
from core.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name="상품명")
    quantity = models.IntegerField(default=1, verbose_name="수량")
    price = models.IntegerField(verbose_name="가격")
    size = models.CharField(max_length=50, blank=True, null=True, verbose_name="크기")
    material = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="제작방식"
    )
    short_description = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="작품 설명"
    )
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING, verbose_name="작가")
    is_soldout = models.BooleanField(default=False, verbose_name="품절 여부")

    class Meta:
        db_table = "product"
        verbose_name = "상품"
        verbose_name_plural = "상품"

    def __str__(self):
        return f"{self.name}"


def get_image_path(instance, filename):
    product = instance.product
    return f"{product.id}/{filename}"


class ProductImage(BaseModel):
    image_url = models.ImageField(
        upload_to=get_image_path, max_length=1000, verbose_name="url"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="상품")
    is_thumbnail = models.BooleanField(default=False, verbose_name="썸네일 여부")

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "product_image"
        verbose_name = "상품 이미지"
        verbose_name_plural = "상품 이미지"
