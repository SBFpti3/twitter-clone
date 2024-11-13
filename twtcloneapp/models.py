from django.db import models

# Create your models here.
class Data(models.Model) :
    username = models.CharField(max_length=20)
    content = models.TextField(default="")