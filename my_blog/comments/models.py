from django.db import models
# from blogs.models import Post
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey('blogs.Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comment on {self.post.title}"