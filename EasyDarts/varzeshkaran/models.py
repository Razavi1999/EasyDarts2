from django.db import models

# Create your models here.
from Account.models import Account


class Race(models.Model):
    name = models.CharField(max_length=100 ,null=False, blank=False)
    holdingDate = models.DateField(null=False, blank=False)
    location = models.TextField(null=False, blank=False)
    conditions = models.TextField(null=False, blank=False)
    EntranceFee = models.IntegerField(null=False, blank=False)
    Awards = models.TextField(null=False, blank=True)
    registrationDate = models.DateField(null=False, blank=False)
    capacity = models.IntegerField(null=False, blank=False)
    #athletes = models.ManyToManyField(Athlete)

class Athlete(Account):
    races = models.ManyToManyField(Race)
    isCoach = False
    isReferee = False
    is_admin = False


class Refree(Account):
    isReferee = True
    CertificationFile = models.FileField(upload_to=None, max_length=254 , null=True)

class Coach(Account):
    isCoach = True
    CertificationFile = models.FileField(upload_to=None, max_length=254 , null=True)


class Club(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, blank=False, max_length=30)
    city = models.CharField(max_length=30 ,null=False, blank=False)
    Images = models.FileField(null=True, blank=True)
    discription = models.TextField(null=True, blank=True)
    AllAwards = models.TextField(null=True, blank=True)


class AdminOfClub(Account):
    is_admin = True
    role = 'ClubAdmin'
    clubId = models.ForeignKey(Club , on_delete=models.CASCADE , default=1)
    CertificationFile = models.FileField(upload_to=None, max_length=254,null=True)

