from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/update/', views.ProfileUpdate.as_view(), name='profile-update'),
    path('accounts/profile/delete/', views.ProfileDelete.as_view(), name='profile-delete'),
    path('post/create/', views.PostCreate.as_view(), name='post-create'),
    path('post/like/<int:pk>', views.like, name='post-like'),
    path('post/detail/<int:pk>', views.PostDetail.as_view(), name='post-detail'),
    path('post/update/<int:pk>', views.PostUpdate.as_view(), name='post-update'),
    path('post/delete/<int:pk>', views.PostDelete.as_view(), name='post-delete'),
    path('comment/create/<int:pk>', views.CommentCreate.as_view(), name='comment-create'),
]