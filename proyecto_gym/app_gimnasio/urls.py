from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('login/',views.login,name='login'),
     path('home/', views.home, name='home'),
     path('logout/', views.logout, name='logout'),
     path('agregarUsuario/', views.agregarUsuario, name='agregarUsuario'),
     path('agregarClase/', views.agregarClase, name='agregarClase'),
]
