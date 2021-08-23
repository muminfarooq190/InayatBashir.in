from PIL import Image
from django.db import models
import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
class Blog(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    image_one = models.ImageField(upload_to='blogs')
    image_two = models.ImageField(upload_to='blogs')
    published_on = models.DateTimeField(auto_now=True)
    is_in_top_three = models.BooleanField(default=False)
    is_top_one = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if not self.id:
            self.image_one = self.compressImage(self.image_one)
            self.image_two = self.compressImage(self.image_two)
        super(Blog , self).save(*args, **kwargs)
    def compressImage(self,uploadedImage):
        imageTemproary = Image.open(uploadedImage)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (1000,530) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return uploadedImage
    

    def __str__(self):
        return self.name

    def  getClassName(self):
        class_name = ...
        return class_name    


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Places(models.Model):
    name = models.ForeignKey(City, related_name = 'places',on_delete=models.CASCADE)
    image_one = models.ImageField(upload_to='places')
    image_two = models.ImageField(upload_to='places')
    description_one = models.CharField(max_length=1000 )
    description_two = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    is_top_one = models.BooleanField(default=False)
    is_in_top_four = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.image_one = self.compressImage(self.image_one)
            self.image_two = self.compressImage(self.image_two)
        super(Places , self).save(*args, **kwargs)
    def compressImage(self,uploadedImage):
        imageTemproary = Image.open(uploadedImage)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (1000,530) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return uploadedImage


    def __str__(self):
        return str(self.name)
