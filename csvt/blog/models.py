from django.db import models

# Create your models here.
sex_choices =(
    ('f','famale'),
    ('t','male'),
)
class User(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1,choices = sex_choices)
    def __str__(self):
        return self.name

