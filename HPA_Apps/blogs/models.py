from django.db import models
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
>>>>>>> 4c0e07bed14186acdf2f886789bf41f52845a520
# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
<<<<<<< HEAD
    title = models.CharField(max_length=200,null=True)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish',null=True)
=======
    title = models.CharField(max_length=200,default="NoName")
    slug = models.SlugField(max_length=200,unique_for_date='publish',default="NoSlug")
>>>>>>> 4c0e07bed14186acdf2f886789bf41f52845a520
    author = models.ForeignKey("users.CustomUser",on_delete=models.CASCADE)
    content = models.TextField(blank=True,null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    upadted = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    image = models.FileField(upload_to='images/',blank=True,null=True)
    draft = models.BooleanField(default=False)


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.publish.year,self.publish.month,self.publish.day,self.slug])

## Name should be edited to take the name of the person
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
