from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from comments.forms import CommentForm
from catagories.models import Catagory
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    posts = Post.objects.order_by('-created_at')[:6]
    return render(request, 'blogs/index.html', {
        'posts': posts
    })


@login_required
def all_blogs(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blogs/all-blogs.html', {
        'posts': posts
    })


@login_required
def blogs_by_date(request):
    posts = Post.objects.order_by('-created_at')[:10]
    return render(request, 'blogs/all-blogs.html', {
        'posts': posts,
        'is_by_date': True
    })


@login_required
def blog_detail(request, post_slug):
    post = get_object_or_404(Post, slug = post_slug)
    comments = post.comments.all().order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('blog_detail', post_slug = post.slug)
    else:
        form = CommentForm()
    
    return render(request, 'blogs/blog-detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })


@login_required
def post_by_catagory(request, slug):
    catagory = get_object_or_404(Catagory, slug = slug)
    posts = catagory.posts.all().order_by('-created_at')
    return render(request, 'blogs/all-blogs.html', {
        'posts': posts,
        'by_catagory': True,
        'catagory': catagory.name
    })


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blogs/add-edit-content.html', {
        'form': form,
        'add_post': True,
        'heading': 'Add New Post'
    })


@login_required
def update_post(request, post_slug):
    post = get_object_or_404(Post, slug = post_slug)
    if post.author != request.user:
        return redirect('blog_detail', post_slug = post_slug)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'blogs/add-edit-content.html', {
        'form': form,
        'edit_post': True,
        'heading': 'Update Post',
    })


@login_required
def delete_blog(request, post_slug):
    post = get_object_or_404(Post, slug = post_slug)

    if post.author != request.user:
       return redirect('blog_detail', post_slug = post_slug)
    
    if request.method == 'POST':
        post.delete()
        return redirect('all_posts')
    
    return render(request, 'blogs/confirm-delete.html', {
        'post': post,
        'delete_post': True
        })


