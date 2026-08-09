from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Content(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    content= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    feature_image = models.ImageField(upload_to="content/")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return  self.title
    
class Meta:
    ordering = ['-title']


class Comment(models.Model):
    content_id = models.ForeignKey(Content,on_delete=models.CASCADE)
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user_id.username} on {self.content_id.title}"

    
