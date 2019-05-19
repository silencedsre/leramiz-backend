from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to='img/about')

    def __str__(self):
        return self.name