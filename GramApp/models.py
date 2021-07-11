from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length =60)
    caption = models.TextField(max_length=300,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete
        
    def __str__(self):
        return self.content

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post_connected=self).count()