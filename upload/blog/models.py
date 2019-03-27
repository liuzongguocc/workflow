from django.db import models

# Create your models here.
class User(models.Model):
    username =models.CharField(max_length =30)
    headImage = models.FileField(upload_to='./upload/')

    def __str__(self):
        return self.username