from django.db import models
from django.contrib.auth.models import User

class Search(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    query = models.TextField(null=False, blank=False)
    saved = models.DateField(auto_now=True)

class Meta:
        ordering = ['-saved']

class SingleResult(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nctId = models.TextField(null=False, blank = False)
    save_date = models.DateField(auto_now=True)

class Meta:
    ordering = ['-save_date']