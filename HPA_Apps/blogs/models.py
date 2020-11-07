from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey("users.CustomUser",on_delete=models.CASCADE)
    content = models.TextField(blank=True,null=True)
    image = models.FileField(upload_to='images/',blank=True,null=True)
