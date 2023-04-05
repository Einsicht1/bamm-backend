from django.db import models

from core.models import BaseModel


class Artist(BaseModel):
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name="작가명")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "artist"
        verbose_name = "작가"
        verbose_name_plural = "작가"
