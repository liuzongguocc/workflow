from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class comp(models.Model):
    name = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee)
    def __str__(self):
        return self.name