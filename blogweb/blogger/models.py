from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tinymce.models import HTMLField
from autoslug import AutoSlugField


class post(models.Model):

    STATUS_CHOICES = (
 ('world', 'World'),
 ('politics', 'Politics'),
 ('india', 'India'),
 ('technology', 'Technology'),
 ('business', 'Business'),
 ('science', 'Science'),
 ('travel', 'Travel'),
 )
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=150, default=None)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    publish = models.DateTimeField(default=timezone.now)
    body = HTMLField()
    status = models.CharField(max_length=10,
 choices=STATUS_CHOICES,
 default='None')
    
    
class Main:
    def __str__(self):
        return self    


    

# Create your models here.
