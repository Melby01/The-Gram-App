from django.test import TestCase
from .models import Image

# Create your tests here.
class ImageTestClass(TestCase):
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
    def test_save_method(self):
        self.new_image.save_image()
        new_image = Image.objects.all()      
        self.assertTrue(len(new_image) >0)
        
    def test_delete_image(self):
        self.new_image.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image)== 0)
        
    def test_update_image(self):
        self.new_image.save_image()
        self.new_image.update_image(self.new_image.id, 'image/test.jpg')
        changed_img = Image.objects.filter(image='image/test.jpg')
        self.assertTrue(len(changed_img) > 0)