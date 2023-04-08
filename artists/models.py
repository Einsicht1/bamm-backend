from django.db import models

from core.models import BaseModel
from users.models import User


class Artist(BaseModel):
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name="작가명")
    user = models.ForeignKey(
        User, verbose_name="유저", blank=True, null=True, on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "artist"
        verbose_name = "작가"
        verbose_name_plural = "작가"
