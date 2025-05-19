# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import User


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # Пример: ручная проверка существования пользователя
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Пользователь с таким логином не существует.")

        # Проверка пароля через authenticate (чтобы не проверять хэш вручную)
        user = authenticate(self.request, username=username, password=password)
        if user is None:
            raise forms.ValidationError("Неверный пароль.")

        self.confirm_login_allowed(user)
        return self.cleaned_data

