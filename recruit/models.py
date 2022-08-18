from email import contentmanager
from sqlite3 import register_converter
from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200)
    nation = models.CharField(max_length=200)
    region = models.CharField(max_length=200)

class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=200)

class Recruit(models.Model):
    recruit_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    position = models.CharField(max_length=200)
    compensation = models.IntegerField(default=0)
    content = models.CharField(max_length=200)
    tech = models.CharField(max_length=200)
    nation = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    volunteer = models.IntegerField(default=0)
# Create your models here.
