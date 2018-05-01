from django.db import models

# Create your models here.

class Client(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.name,self.email)