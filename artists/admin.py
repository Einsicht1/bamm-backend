from django.contrib import admin
from django.contrib.admin import ModelAdmin

from artists.models import Artist


class ArtistAdmin(ModelAdmin):
    exclude = [
        "deleted_at",
    ]


admin.site.register(Artist, ArtistAdmin)

# Register your models here.
