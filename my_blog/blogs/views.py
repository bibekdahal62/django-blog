from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Catagory
from .forms import CommentForm

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


def catagories_list(request):
    catagories = Catagory.objects.order_by('name')
    return render(request, 'blogs/catagories.html', {
        'catagories' : catagories
    })


def post_by_catagory(request, slug):
    catagory = get_object_or_404(Catagory, slug = slug)
    posts = Post.objects.filter(catagory = catagory)
    return render(request, 'blogs/all-blogs.html', {
        'posts': posts,
        'by_catagory': True,
        'catagory': catagory.name
    })


def update_comment(request, post_slug, comment_id):
    comment = get_object_or_404(Comment, pk = comment_id)
    if comment.user != request.user:
        return redirect('blog_detail', post_slug = post_slug)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', post_slug = post_slug)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blogs/edit-content.html', {
        'form': form,
        'comment': comment,
        'post_slug': post_slug,
        'edit_action_for_comment': True
    })