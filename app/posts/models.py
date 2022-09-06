from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(max_length=20, verbose_name=_("제목"))
    body = models.CharField(max_length=200, verbose_name=_("본문"))
    password = models.CharField(max_length=255, verbose_name=_("비밀번호"))

    def __str__(self):
        return self.title
