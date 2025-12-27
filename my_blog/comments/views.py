from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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
    return render(request, 'blogs/add-edit-content.html', {
        'form': form,
        'comment': comment,
        'post_slug': post_slug,
        'edit_comment': True,
        'heading': "Update Comment"
    })


@login_required
def delete_comment(request, post_slug, id):
    comment = get_object_or_404(Comment, pk = id)

    if comment.user != request.user:
       return redirect('blog_detail', post_slug = post_slug)
    
    if request.method == 'POST':
        comment.delete()
        return redirect('all_posts')
    
    return render(request, 'blogs/confirm-delete.html', {
        'delete_comment': True,
        'post_slug': post_slug,
        'comment': comment
        })