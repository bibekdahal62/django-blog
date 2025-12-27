from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_at')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Post, PostAdmin)
