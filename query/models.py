from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.TextField()

    def __str__(self):
        return self.name

class department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class entry(models.Model):
    block = models.ForeignKey(student, on_delete=CASCADE)
    discript = models.CharField(max_length=100)
    admit = models.DateField()
    # users = models.OneToOneField(student)
    rating = models.IntegerField()

    def __str__(self):
        return self.discript

