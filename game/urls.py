from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import MasterAuthenticationForm, PlayerAuthenticationForm
from .views import (
    dashboard_master, dashboard_player,
    char_levelup, char_applyDamage
    )

app_name = 'game'

urlpatterns = [
    path('master/', dashboard_master),
    path('master/login/', auth_views.login, {'template_name': 'game/login.html',
        'authentication_form': MasterAuthenticationForm}, name='login'),

    path('player/', dashboard_player),
    path('player/login/', auth_views.login, {'template_name': 'game/login.html',
        'authentication_form': PlayerAuthenticationForm}, name='login'),

    path('logout/', auth_views.logout, {'template_name': 'game/logged_out.html'}, name='logout'),
    path('<int:char_id>/levelup', char_levelup, name='char_levelup'),
    path('<int:char_id>/<int:damage>/applydamage', char_applyDamage, name='char_applyDamage')
]
