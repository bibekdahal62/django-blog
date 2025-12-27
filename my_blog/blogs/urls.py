from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/', views.all_blogs, name='all_posts'),
    path('posts-by-date/', views.blogs_by_date, name = 'posts_by_date'),
    path('post-details/<slug:post_slug>', views.blog_detail, name= 'blog_detail'),
    path('catagories/', views.catagories_list, name='catagories'),
    path('post/catagory/<slug:slug>', views.post_by_catagory, name='blog_by_catagory'),
    path('update-comment/<slug:post_slug>/<int:comment_id>', views.update_comment, name='update_comment'),
    path('add-post', views.add_post,name='add_blog'),
    path('update-post/<slug:post_slug>', views.update_post,name='update_blog'),
    path('delete-post/<slug:post_slug>', views.delete_blog, name='delete_blog'),
    path('delete-comment/<slug:post_slug>/<int:id>', views.delete_comment, name='delete_comment')

]