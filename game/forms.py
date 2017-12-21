from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()

class MasterAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.master:
            raise forms.ValidationError("you're a simple player", code='invalid_login')

    class Meta(AuthenticationForm):
        model = User
        fields = ('username', 'password')

class PlayerAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if user.master:
            raise forms.ValidationError('please login in master/', code='invalid_login')

    class Meta(AuthenticationForm):
        model = User
        fields = ('username', 'password')
