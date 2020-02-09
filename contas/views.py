from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView
from .forms import EcommerceAuthenticationForm, EcommerceUserCreateForm
from .models import EcommerceUser
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login


class EcommerceLogin(LoginView):
    template_name = 'contas/login.html'
    authentication_form = EcommerceAuthenticationForm

class EcommerceLogout(LogoutView):
    next_page = reverse_lazy('home')

class UserPerfil(TemplateView):
    template_name = 'contas/user_perfil.html'
    model = EcommerceUser

class EcommerceUserCreate(CreateView):
    template_name = 'contas/create_user.html'
    form_class = EcommerceUserCreateForm
    success_url = reverse_lazy('login')

