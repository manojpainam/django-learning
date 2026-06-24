from django.db import models

# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mobile = models.IntegerField(null=True)

    def __str__(self):
        return "{} {}".format(self.fname, self.lname)