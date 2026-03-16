from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
