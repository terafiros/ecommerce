from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from produtos.models import CarrinhoCompras

class EcommerceUser(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    carrinho = models.OneToOneField(CarrinhoCompras, blank=True, null=True, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


