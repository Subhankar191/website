# from django.db import models

# Create your models here

from django.db import models

class Info(models.Model):
    username = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)  # Store hashed password

    def __str__(self):
        return self.username