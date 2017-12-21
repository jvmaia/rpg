from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import PlayerUser

class PlayerAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_master:
            raise forms.ValidationError('problem', code='invalid_login')

    class Meta(AuthenticationForm):
        model = PlayerUser
        fields = ('username', 'password')
