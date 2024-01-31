from django.db import models

# Create your models here.
class book(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    des=models.CharField(max_length=50)

    def __str__(self):
        return self.name
