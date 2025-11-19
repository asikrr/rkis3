from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Post


class SignUpForm(UserCreationForm):
    avatar = forms.ImageField(label='Изображение профиля')

    class Meta:
        model = CustomUser
        fields = ['username', 'avatar', 'password1', 'password2']


class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {'title': 'Название', 'content': 'Текст'}