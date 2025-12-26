from django.contrib import admin
from .models import Post, Comment, Catagory

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_at')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'text', 'created_at')
    list_filter = ('post', )


class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    list_filter = ('name', )
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Catagory, CatagoryAdmin)