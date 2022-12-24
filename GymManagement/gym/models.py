from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=11)
    emailid = models.CharField(max_length=60)
    age = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=11)
    unit = models.CharField(max_length=10)
    date = models.CharField(max_length=40)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=60)
    amount = models.CharField(max_length=11)
    duration = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=11)
    emailid = models.CharField(max_length=60)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    plan = models.CharField(max_length=50)
    joindate = models.CharField(max_length=40)
    expiredate= models.CharField(max_length=40)
    initialamount = models.CharField(max_length=10)

    def __str__(self):
        return self.name
