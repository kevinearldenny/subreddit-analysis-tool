from django.contrib import admin
from .models import User, Subreddit, Post
# Register your models here.

admin.site.register(User)
admin.site.register(Subreddit)
admin.site.register(Post)

