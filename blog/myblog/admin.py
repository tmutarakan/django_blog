from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'post', 'text', 'created_date')
    list_filter = ('username', 'created_date')
    search_fields = ('username', 'text')
