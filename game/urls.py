from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', dashboard),
    path('login/', auth_views.login, {'template_name': 'core/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'core/logged_out.html'}, name='logout')
]
