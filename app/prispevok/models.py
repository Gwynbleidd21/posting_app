"""
Database models
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Prispevok(models.Model):
    title = models.CharField(max_length=200, unique=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='prispevky'
    )
    body = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('prispevok', kwargs={'pk': self.pk})
