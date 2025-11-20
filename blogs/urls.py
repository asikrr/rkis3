from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    path('post/create/', views.PostCreate.as_view(), name='post-create'),
    path('post/like/<int:pk>', views.like, name='post-like'),
]