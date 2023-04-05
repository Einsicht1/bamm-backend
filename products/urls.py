from django.contrib import admin
from django.urls import path

from products.views import ProductListAPIView, ProductDetailAPIView

urlpatterns = [
    path("products", ProductListAPIView.as_view()),
    path("products/<int:pk>", ProductDetailAPIView.as_view()),

]
