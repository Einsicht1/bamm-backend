from rest_framework import serializers

from artists.serializers import ArtistSerializer
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        return [image_obj.image_url.url for image_obj in obj.productimage_set.all()]

    class Meta:
        model = Product
        fields = "__all__"
