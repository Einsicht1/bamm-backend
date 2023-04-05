# Generated by Django 4.1.7 on 2023-04-02 23:15

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='상품명')),
                ('quantity', models.IntegerField(default=1, verbose_name='수량')),
                ('price', models.IntegerField(verbose_name='가격')),
                ('size', models.CharField(blank=True, max_length=50, null=True, verbose_name='크기')),
                ('material', models.CharField(blank=True, max_length=50, null=True, verbose_name='제작방식')),
                ('short_description', models.CharField(blank=True, max_length=50, null=True, verbose_name='작품 설명')),
                ('is_soldout', models.BooleanField(default=False, verbose_name='품절 여부')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='artists.artist', verbose_name='작가')),
            ],
            options={
                'verbose_name': '상품',
                'verbose_name_plural': '상품',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('image_url', models.ImageField(max_length=1000, upload_to=products.models.get_image_path, verbose_name='url')),
                ('is_thumbnail', models.BooleanField(default=False, verbose_name='썸네일 여부')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='상품')),
            ],
            options={
                'verbose_name': '상품 이미지',
                'verbose_name_plural': '상품 이미지',
                'db_table': 'product_image',
            },
        ),
    ]
