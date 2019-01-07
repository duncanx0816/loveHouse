from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime


class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    body = models.TextField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)

    @property
    def created_str(self):
        return datetime.strftime(self.created, '%y/%m/%d')

    @property
    def gender(self):
        return self.author.username == 'Duncan'
