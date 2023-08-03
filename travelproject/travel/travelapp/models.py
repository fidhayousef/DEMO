from django.db import models

# Create your models here.
class Place(models.Model):
    name= models.CharField(max_length=250)
    img= models.ImageField(upload_to="pics")
    desc= models.TextField()

class People(models.Model):
    im= models.ImageField(upload_to="pics")
    na= models.CharField(max_length=150)
    des= models.TextField()

    def __str__(self):
        return self.name

    def __str__(self):
        return self.na



