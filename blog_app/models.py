from django.db import models
from datetime import datetime
from djgeojson.fields import PointField
# from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    is_active = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.SlugField(max_length=100)
    categories = models.ManyToManyField('blog_app.Category')

    def __str__(self):
        return self.title

    
    # @property
    # def days_since_creations(self):
    #     diff = timezone.now() - self.list_date
    #     return diff.days


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text



class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'



class Place(models.Model):
    name = models.CharField(max_length=255)
    location = PointField()

    def __str__(self):
        return self.name