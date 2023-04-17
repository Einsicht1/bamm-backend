from django.contrib import admin
from django.contrib.admin import ModelAdmin

from products.models import Product, ProductImage


class InlineProductImage(admin.StackedInline):
    model = ProductImage
    max_num = 5
    exclude = [
        "deleted_at",
    ]


class ProductAdmin(ModelAdmin):
    inlines = [InlineProductImage]
    exclude = [
        "deleted_at",
    ]
    list_display = [
        "pk",
        "artist",
        "is_soldout",
        "material",
        "name",
        "price",
        "quantity",
        "short_description",
        "size",
    ]


admin.site.register(Product, ProductAdmin)

# Register your models here.
