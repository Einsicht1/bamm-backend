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


admin.site.register(Product, ProductAdmin)

# Register your models here.
