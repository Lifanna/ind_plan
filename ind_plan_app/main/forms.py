import unicodedata
from .auth_backend import CustomBackend
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    login = forms.CharField(max_length=30, required=True)
    password = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ['login', 'password',]
        error_messages = {
            'login': {
                'required': "Пожалуйста, введите логин",
                'unique': "Пользователь с таким логином уже существует"
            },
            'password': {
                'required': "Пожалуйста, введите пароль"
            }
        }

class UsernameField(forms.CharField):
    def to_python(self, value):
        return unicodedata.normalize('NFKC', super().to_python(value))

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            'autocapitalize': 'none',
            'autocomplete': 'username',
        }


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            custom_backend = CustomBackend()
            self.user_cache = custom_backend.authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    error_messages = {
        'invalid_login': (
            "Неправильный логин/пароль"
        ),
        'inactive': "Данный аккаунт неактивный",
    }
