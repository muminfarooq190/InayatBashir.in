from PIL import Image
from django.db import models

class Blog(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    image_one = models.ImageField(upload_to='blogs')
    image_two = models.ImageField(upload_to='blogs')
    published_on = models.DateTimeField(auto_now=True)
    is_in_top_three = models.BooleanField(default=False)
    is_top_one = models.BooleanField(default=False)

  

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
    is_in_top_four = models.BooleanField(default=False)

  


    def __str__(self):
        return str(self.name)
