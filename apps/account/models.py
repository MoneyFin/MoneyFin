from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from datetime import timezone
from apps.core.models import BaseModel


class CustomUser(BaseModel, AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    national_id = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
