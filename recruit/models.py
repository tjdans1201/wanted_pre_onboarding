from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200)
    nation = models.CharField(max_length=200)
    region = models.CharField(max_length=200)

class Recruit(models.Model):
    recruit_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    compensation = models.IntegerField(default=0)
    content = models.CharField(max_length=200)
    tech = models.CharField(max_length=200)
    nation = models.CharField(max_length=200)
    region = models.CharField(max_length=200)

class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=200)
    applied_recruiting = models.IntegerField(null= True, blank= True)

class AppliedHistory(models.Model):
    recruit_id = models.IntegerField(null= True, blank= True)
    member_id = models.IntegerField(null= True, blank= True)
# Create your models here.
