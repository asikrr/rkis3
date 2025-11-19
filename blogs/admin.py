from django.contrib import admin

from blogs.models import Post, Comment, CustomUser, Like

admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)