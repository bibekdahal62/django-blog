from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=100, default='Others')
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"
    

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Catagory.objects.filter(slug = slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name="catagory")
    
    def __str__(self):
        return f"{self.title}"
    

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug = slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comment on {self.post.title}"
    
