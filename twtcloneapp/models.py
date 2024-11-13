from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Data(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    content = models.TextField(default="")