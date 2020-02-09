from django.urls import path
from .views import EcommerceLogin, UserPerfil, EcommerceLogout, EcommerceUserCreate

urlpatterns = [
    path('login', view=EcommerceLogin.as_view(), name='login'),
    path('perfil', view=UserPerfil.as_view(), name='perfil'),
    path('logout', view=EcommerceLogout.as_view(), name='logout'),
    path('criar', view=EcommerceUserCreate.as_view(), name='criar-usuario')
]