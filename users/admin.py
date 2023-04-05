from django.contrib import admin
from django.contrib.admin import ModelAdmin

from users.models import User


class UserAdmin(ModelAdmin):
    exclude = ["deleted_at",]



admin.site.register(User, UserAdmin)


# Register your models here.
