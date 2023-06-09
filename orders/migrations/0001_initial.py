# Generated by Django 4.1.7 on 2023-04-12 23:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0002_alter_product_short_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "order_number",
                    models.CharField(max_length=200, unique=True, verbose_name="주문번호"),
                ),
                ("quantity", models.IntegerField(default=1, verbose_name="수량")),
                (
                    "total_amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=13, verbose_name="결제 금액"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("결제 대기", "Payment Pending"),
                            ("결제 완료", "Payment Completed"),
                            ("배송 대기", "Shipping Pending"),
                            ("배송 중", "Shipping In Progress"),
                            ("배송 완료", "Shipping Completed"),
                            ("구매 확정", "Purchase Confirmed"),
                        ],
                        default="결제 대기",
                        max_length=50,
                        verbose_name="주문 상태",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="products.product",
                        verbose_name="상품",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="유저",
                    ),
                ),
            ],
            options={
                "verbose_name": "주문",
                "verbose_name_plural": "주문",
                "db_table": "orders",
            },
        ),
    ]
