from django.db import models
from django.utils import timezone
# Create your models here.
from datetime import datetime

class Pet(models.Model):
    name_text = models.CharField(max_length=200)
    breed_text = models.CharField(max_length=100)
    color_text = models.CharField(max_length=100)
    age_text = models.CharField(max_length=100)
    size_text = models.CharField(max_length=100)
    sex_text = models.CharField(max_length=100)
    info_text = models.CharField(max_length=500)
    story_text = models.CharField(max_length=1000)
    model_pic = models.ImageField(upload_to='images',default='pic_folder/None/no-img.jpg')
    pub_date = models.DateTimeField("date published",default=datetime.now)
    def __str__(self):
        return self.name_text


class Article(models.Model):

    title = models.CharField(max_length=100)
    section = models.CharField(max_length=1000)
    pub_date = models.DateTimeField("date published")
    model_pic = models.ImageField(upload_to='images',default='pic_folder/None/no-img.jpg')
    theme = models.CharField(max_length=100,default='none')
    def __str__(self):
        return self.title

