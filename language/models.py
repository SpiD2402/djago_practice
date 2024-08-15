from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=100)
    extension=models.CharField(max_length=15)
    user= models.ForeignKey(User,on_delete=models.CASCADE,related_name='languages')
    class Meta:
        db_table='languages'

    def __str__(self):
        return self.name

