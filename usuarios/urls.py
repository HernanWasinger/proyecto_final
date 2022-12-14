from django.urls import path
from usuarios.views import *
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('editarPerfil/', views.editarPerfil, name="editarPerfil"),
    path('Perfil/', views.Perfil, name="Perfil"),
    path('editar_imagen/', EditarPerfilImage, name='EditarPerfilImage'),
]