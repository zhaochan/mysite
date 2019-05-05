from django.db import models

# Create your models here.
class Grade(models.Model):
     name = models.CharField(max_length=20)
     studentnum = models.IntegerField()
     girlnum = models.IntegerField()
     boynum = models.IntegerField()
     
     class Meta:
       db_table='grade'

# Create your models here.
