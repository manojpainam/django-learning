from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=20, null=False, unique=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mobile = models.BigIntegerField(null=True)

    def __str__(self):
        return "{} {}".format(self.fname, self.lname)