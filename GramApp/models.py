from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length =60)
    # description = models.CharField(max_length =200)
    pub_date = models.DateTimeField(auto_now_add=True)
    Images_image = models.ImageField(upload_to = 'images/')
    caption = models.CharField(max_length =60)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # comment = models.TextField(blank=True)
    post = HTMLField()
    

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
           
    @classmethod
    def search_by_name(cls,search_term):
        image = cls.objects.filter(name__icontains=search_term)
        return image
     
         
    @classmethod
    def update_caption(cls, id, value):
        cls.objects.filter(id=id).update(name = value)
        
    def __str__(self):
        return self.name
       


class Profile(models.Model):
    photo = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length =200)
    name = models.OneToOneField(User,on_delete=models.CASCADE)


    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
    @classmethod
    def search_by_name(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return photo
    def __str__(self):
        return self.bio 
    
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name  
      
class Comment(models.Model):
    comment = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE )
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def save_comment(self):
        self.save()
        
    def delete_comment(self):
        self.delete()
        
    @classmethod
    def update_comment(cls, id, value):
        cls.objects.filter(id=id).update(name = value)
        
    def __str__(self):
        return self.comment  
