from django.urls import path
from usuarios.views import login_request, register
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    #path('editarPerfil/', views.editarPerfil, name="EditarPerfil")
]