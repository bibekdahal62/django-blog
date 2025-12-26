from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': 'Leave a comment'
        }
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Write your comment here...',
                'class': 'comment-textarea'
            }),
        }

#{% url 'add_comment' post.slug %}