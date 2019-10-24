"""Posts admin classes"""

# Django
from django.contrib import admin

# Models
from posts.models import Post

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    """Posts admin"""

    list_display = ('pk', 'user', 'profile', 'title', 'photo')
