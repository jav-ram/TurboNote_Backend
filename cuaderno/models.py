from django.db import models
from django.contrib.auth.models import User

# Create your models here. Cuaderno
class Notebook(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)