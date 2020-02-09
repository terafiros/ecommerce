from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import EcommerceUser
from django.contrib.auth.forms import UserCreationForm


class EcommerceAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Senha',
        required=True
    )

    class Meta:
        model = EcommerceUser

class EcommerceUserCreateForm(UserCreationForm):

    class Meta:
        fields = ['username','email', 'password1', 'password2']
        model = EcommerceUser


