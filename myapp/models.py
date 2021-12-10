from django.db import models

class Stud(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    mobileNo = models.IntegerField(max_length=20)
    email = models.EmailField(max_length=50)
    age = models.IntegerField(max_length=20)
    education = models.CharField(max_length=80)
    #docs = models.CharField(max_length=20)
    SrNo = models.IntegerField(max_length=20)
    qualification = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    passingYear = models.IntegerField(max_length=20)
    percentage = models.FloatField(max_length=20)
    #images = models.FileField()    

    