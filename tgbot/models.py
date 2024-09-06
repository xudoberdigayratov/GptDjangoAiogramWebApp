from django.db import models
from django.utils import timezone


# Create your models here.

class Users(models.Model):
    user_id = models.CharField(max_length=250)
    name = models.CharField(max_length=250, null=True, blank=True)
    limited = models.IntegerField(default=10)
    created_at = models.DateTimeField(default=timezone.now, null=False)
    lasted_at = models.DateTimeField(default=timezone.now, null=False)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.user_id


class Chat(models.Model):
    user_id = models.CharField(max_length=250)
    message = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, null=False)

    class Meta:
        verbose_name_plural = "Chat"

    def __str__(self):
        return self.user_id
