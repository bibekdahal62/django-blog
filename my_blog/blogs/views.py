from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Catagory

# Create your views here.

def index(request):
    posts = Post.objects.order_by('-created_at')[:6]
    return render(request, 'blogs/index.html', {
        'posts': posts
    })


def all_blogs(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blogs/all-blogs.html', {
        'posts': posts
    })


def blogs_by_date(request):
    posts = Post.objects.order_by('-created_at')[:10]
    return render(request, 'blogs/all-blogs.html', {
        'posts': posts,
        'is_by_date': True
    })


def blog_detail(request, post_slug):
    post = get_object_or_404(Post, slug = post_slug)
    return render(request, 'blogs/blog-detail.html', {
        "post" : post
    })


def catagories_list(request):
    catagories = Catagory.objects.all()
    return render(request, 'blogs/catagories.html', {
        'catagories' : catagories
    })


def post_by_catagory(request, slug):
    pass