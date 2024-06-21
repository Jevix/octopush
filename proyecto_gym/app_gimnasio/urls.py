from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
     path('login/', views.index, name='index'),
=======
     path('', views.index, name='index'),
     path('login/',views.login,name='login'),
>>>>>>> origin/backend
     path('home/', views.home, name='home'),
     path('logout/', views.logout, name='logout')
]
