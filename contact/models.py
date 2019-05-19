from django.db import models

# Create your models here.

class ContactInquiry(models.Model):
    name = models.CharField(max_length=150, null=True)
    email = models.EmailField(null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name + " : " + self.message