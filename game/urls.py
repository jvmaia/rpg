from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import PlayerAuthenticationForm
from .views import dashboard

urlpatterns = [
    path('', dashboard),
    path('login/', auth_views.login, {'template_name': 'core/login.html',
        'authentication_form': PlayerAuthenticationForm}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'core/logged_out.html'}, name='logout')
]
