from django.db import models
 
 
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
 
    def __unicode__(self):  # __str__ on Python 3
        return self.name