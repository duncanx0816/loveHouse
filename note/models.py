from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    body = models.TextField()
    created = models.DateField(auto_now_add=True)