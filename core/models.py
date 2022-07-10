from django.db import models

class Product (models.Model):
    picture = models.FileField()
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    rate = models.IntegerField(default=5)
    description = models.TextField(max_length=500)

    def __str__(self):
        return 'Product ' + self.name

class Request (models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return 'Name: ' + self.name
