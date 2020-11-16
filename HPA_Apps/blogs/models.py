from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import UserManager
# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    title = models.CharField(max_length=200,null=True)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish',null=True)
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

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type


## Name should be edited to take the name of the person
class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        obj_id = instance.id
        qs = super(CommentManager, self).filter(object_id=obj_id).filter(parent=None)
        return qs



class Comment(models.Model):
    '''
     Don't use the content type or object id
    '''

    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,null=True, blank=True)
    object_id = models.AutoField(primary_key=True)
    # content_object = GenericForeignKey('content_type', 'object_id')

    author = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    parent = models.ForeignKey("self", null=True, blank=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    objects = CommentManager()
    class Meta:
        ordering = ('created',)


    def __str__(self):
        return str(self.author.first_name)

    def children(self): #replies
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
