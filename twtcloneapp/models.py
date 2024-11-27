from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Data(models.Model) :
    username = models.CharField(max_length=150, default="")
    content = models.TextField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", null=True, blank=True) # buat hapus post kalau akun user dihapus