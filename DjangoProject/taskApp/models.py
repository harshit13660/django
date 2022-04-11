from django.db import models


class userData(models.Model):
    userName=models.CharField(max_length=100)
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.userName

