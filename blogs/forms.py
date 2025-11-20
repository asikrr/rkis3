from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Post, Comment


class SignUpForm(UserCreationForm):
    avatar = forms.ImageField(label='Изображение профиля')

    class Meta:
        model = CustomUser
        fields = ['username', 'avatar', 'bio', 'password1', 'password2']


class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {'title': 'Название', 'content': 'Текст'}


class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']