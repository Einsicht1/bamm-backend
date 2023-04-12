from rest_framework import serializers

from artists.serializers import ArtistSerializer
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    thumbnail = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    def get_thumbnail(self, obj):
        if thumbnail := obj.productimage_set.filter(is_thumbnail=True).first():
            return thumbnail.image_url.url

        if first_image := obj.productimage_set.first():
            return first_image.image_url.url
        return None

    def get_images(self, obj):
        return [
            image_obj.image_url.url
            for image_obj in obj.productimage_set.filter(is_thumbnail=False)
        ]

    class Meta:
        model = Product
        fields = "__all__"


class ShippingPolicySerializer(serializers.Serializer):
    method = serializers.CharField(default="DELIVERY")
    feeType = serializers.CharField(default="FREE")
    feePayType = serializers.CharField(default="FREE")
    feePrice = serializers.CharField(default="0")


class NaverPayProductValidationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    basePrice = serializers.IntegerField(source="price")
    taxType = serializers.CharField(default="TAX_FREE")
    infoUrl = serializers.SerializerMethodField()
    imageUrl = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    shippingPolicy = serializers.SerializerMethodField()

    def get_infoUrl(self, instance):
        return f"https://bamm.kr/detail/{instance.id}"

    def get_imageUrl(self, instance):
        return instance.productimage_set.filter(is_thumbnail=True).first().image_url.url

    def get_status(self, instance):
        return "ON_SALE" if not instance.is_soldout else "SOLDOUT"

    def get_shippingPolicy(self, instance):
        return ShippingPolicySerializer(1).data
