from django.contrib import admin
from .models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'text', 'created_at')
    list_filter = ('post', )


admin.site.register(Comment, CommentAdmin)