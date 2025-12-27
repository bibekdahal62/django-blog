from django.db import models
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