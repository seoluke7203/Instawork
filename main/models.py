from django.db import models

# Create your models here.
class List(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.email