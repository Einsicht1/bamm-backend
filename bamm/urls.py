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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from core.views import HealthCheckView
from orders.views import OrderCreateAPIView, PortOneWebhookAPIView
from products.views import (
    NaverPayProductValidationAPIVIew,
    ProductDetailAPIView,
    ProductListAPIView,
)
from users.views import KakakoSocialLoginAPIVIew

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", HealthCheckView.as_view()),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/products", ProductListAPIView.as_view()),
    path("api/v1/products/<int:pk>", ProductDetailAPIView.as_view()),
    path("api/v1/users/sign-in/kakao", KakakoSocialLoginAPIVIew.as_view()),
    path(
        "api/v1/naverpay/product-validation", NaverPayProductValidationAPIVIew.as_view()
    ),
    path("api/v1/orders", OrderCreateAPIView.as_view(), name="order-create"),
    path("api/v1/portone-webhook", PortOneWebhookAPIView.as_view()),
    path("accounts/", include("allauth.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("", HealthCheckView.as_view()),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
