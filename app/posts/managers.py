from django.db import models
from django.contrib.auth.hashers import make_password


class PostManager(models.Manager):
    def create(self, title, body, password):
        hashed_password = make_password(password)
        post = super().create(title=title, body=body, password=hashed_password)
        return post
