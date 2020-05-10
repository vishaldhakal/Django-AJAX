from django.db import models

class userModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)