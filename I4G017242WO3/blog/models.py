from typing import Text
from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Post(models.Model):
    Title = models.CharField(max_length=200, unique=True)
    Author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    Text = models.TextField()
    Published_date = models.DateTimeField(auto_now= True)
    Created_date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title

# Create your models here.
