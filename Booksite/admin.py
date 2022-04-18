from django.contrib import admin
from .models import Post, Profile, Comment #, branch
# Register your models here.
admin.site.register(Post)
# admin.site.register(branch)
admin.site.register(Profile)
admin.site.register(Comment)