from django.db import models

# Create your models here.
class Data(models.Model) :
    nama = models.CharField(max_length=20)
    message = models.TextField(default="")