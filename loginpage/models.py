from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)

    def creation(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.username
