from django.contrib import admin
from django.urls import path
from .views import index, aventura, plataforma, guerra, terror, rpg, registro
from django.contrib.auth import views as auth_views
from .views import MyPasswordChangeView

urlpatterns = [
    path('', index, name='index'),
    #catalogo de videojuegos
    path('catalogo/aventura/', aventura, name='aventura'),
    path('catalogo/plataforma/', plataforma, name='plataforma'),
    path('catalogo/guerra/', guerra, name='guerra'),
    path('catalogo/terror/', terror, name='terror'),
    path('catalogo/rpg/', rpg, name='rpg'),
    #registro
    path('registro/', registro, name='registro'),
    #cambiar contraseña
    path('password_change/', MyPasswordChangeView.as_view(), name='password_change'),
]

