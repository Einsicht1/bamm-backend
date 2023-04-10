from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models, transaction

from core.models import BaseModel


class CustomUserManager(UserManager):
    @transaction.atomic
    def create_social_login_user(self, email: str, *args, **kwargs):
        user = self.model(email=email)
        user.save()
        SocialLoginPlatform.objects.create(
            name="kakao", social_login_id=kwargs.get("social_login_id"), user=user
        )
        return user


class User(AbstractUser, BaseModel):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
        verbose_name = "회원 관리"
        verbose_name_plural = "회원 관리"


class SocialLoginPlatform(BaseModel):
    name = models.CharField(max_length=20)
    social_login_id = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        db_table = "social_login_platform"
        verbose_name = "소셜 로그인 플랫폼"
        verbose_name_plural = "소셜 로그인 플랫폼"
