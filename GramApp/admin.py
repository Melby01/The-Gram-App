from django.contrib import admin
from .models import Image,tags,Comment
# Register your models here.


admin.site.register(Image)
 
admin.site.register(tags)
admin.site.register(Comment)
