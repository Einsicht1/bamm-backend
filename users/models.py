from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from core.models import BaseModel


# models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class UserManager(BaseUserManager):
    # TODO: override 해야함.
    def create_user(self, email, username, password=None):
        pass
        # if not email:
        #     raise ValueError('Users must have an email address')
        #
        # user = self.model(
        #     email=self.normalize_email(email),
        #     username=username,
        # )
        #
        # user.set_password(password)
        # user.save(using=self._db)
        # return


class User(AbstractBaseUser, BaseModel):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
        verbose_name = "회원 관리"
        verbose_name_plural = "회원 관리"
