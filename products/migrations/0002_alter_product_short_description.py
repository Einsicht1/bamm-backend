# Generated by Django 4.1.7 on 2023-04-11 23:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="short_description",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="작품 설명"
            ),
        ),
    ]