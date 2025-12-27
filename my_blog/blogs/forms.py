from django import forms
from .models import Post


#{% url 'add_comment' post.slug %}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'catagory']
        labels = {
            'title': 'Title',
            'content': 'Description',
            'image': 'Choose an image',
            'catagory': 'Choose an Catagory'
        }
        widgets = {
            'title': forms.TextInput(attrs = {
                'placeholder': 'Enter the title',
                'class': 'post-title'
            }),
            'content': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'description here...',
                'class': 'post-content'
            })
        }