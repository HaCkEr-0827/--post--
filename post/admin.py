from django.contrib import admin
from .models import CustomUser, Category, Post, Comment



admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'comment_count')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'text')