from django.db import models

class Course(models.Model):
    cname = models.CharField(max_length=30)

    def __str__(self):
        return self.cname

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    # course = models.CharField(max_length=45)#normal table
    course = models.ForeignKey(Course,on_delete=models.CASCADE)#we link one table into another
    phone = models.BigIntegerField(default=0)
    email = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return (f'{self.name} , {self.course}')
