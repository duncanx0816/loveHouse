from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime


class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todoes')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    @property
    def created_str(self):
        return datetime.strftime(self.created, '%y/%m/%d %H:%M')
