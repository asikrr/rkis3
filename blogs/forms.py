from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class SignUpForm(UserCreationForm):
    avatar = forms.ImageField(label='Изображение профиля')

    class Meta:
        model = CustomUser
        fields = ['username', 'avatar', 'password1', 'password2']