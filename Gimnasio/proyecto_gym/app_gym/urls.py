from django.urls import path
from . import views
from django.urls import path
from .views import IndexView, HomeView
from .components import home, login

urlpatterns = [
    path('', IndexView),
    path('home/', HomeView),
    path('reactpy/index/', login, name='reactpy_login'),
    path('reactpy/home/', home, name='reactpy_home'),
]
