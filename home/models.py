from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class HeroImage(models.Model):
    """
    Model to store hero images for the home page.
    """
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title
    
class ImageGallery(models.Model):
    """
    Model to store images for the image gallery.
    """
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title
