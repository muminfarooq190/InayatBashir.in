
from django.db import models

class Blog(models.Model):

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)
    image_one = models.ImageField()
    image_two = models.ImageField()
    published_on = models.DateTimeField(auto_now=True)
    is_in_top_three = models.BooleanField(default=False)
    is_top_one = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Places(models.Model):
    name = models.ForeignKey(City,on_delete=models.CASCADE)
    image_one = models.ImageField()
    image_two = models.ImageField()
    description_one = models.CharField(max_length=1000 )
    description_two = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
