from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15,default='')


    def __str__(self):
        return self.full_name
