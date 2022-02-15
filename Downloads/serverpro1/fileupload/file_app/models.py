from django.db import models

# Create your models here.

GENDER_CHOICES = (
    (str(0), 'male'),
    (str(1), 'female'),
    (str(2), 'not specified'),
)

class Employee(models.Model):
    name = models.CharField(max_length=50,blank=False, null=False)
    email = models.CharField(max_length=20)
    number = models.IntegerField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    company = models.CharField(max_length=50,blank=False)
    emp_id = models.IntegerField(null=False)
    manager = models.CharField(max_length=50, null=False)