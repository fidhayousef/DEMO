from django.db import models


# Create your models here.


class store(models.Model):
    itemname = models.CharField(max_length=50)
    itemdesc = models.TextField()


def __str__(self):
    return self.itemname
