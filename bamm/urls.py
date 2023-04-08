"""bamm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from core.views import HealthCheckView
from products.views import ProductDetailAPIView, ProductListAPIView
from users.views import KakakoSocialLoginAPIVIew

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", HealthCheckView.as_view()),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/products", ProductListAPIView.as_view()),
    path("api/v1/products/<int:pk>", ProductDetailAPIView.as_view()),
    path("api/v1/users/sign-in/kakao", KakakoSocialLoginAPIVIew.as_view()),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
