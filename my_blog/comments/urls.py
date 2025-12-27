from django.urls import path
from . import views

urlpatterns = [
    path('update-comment/<slug:post_slug>/<int:comment_id>', views.update_comment, name='update_comment'),
    path('delete-comment/<slug:post_slug>/<int:id>', views.delete_comment, name='delete_comment'),
]