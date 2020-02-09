from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class EcommerceUser(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


