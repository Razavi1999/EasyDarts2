from rest_framework import serializers
from Account.models import Account
from varzeshkaran.models import *


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = ['image', 'first_name', 'last_name', 'ageType']



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = ['image', 'first_name', 'last_name', 'ageType']



class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ['name' , 'holdingDate' , 'location' , 'EntranceFee']

class RefreeSerializer(serializers.ModelSerializer):
    CertificationFile = serializers.FileField()

    class Meta:
        model = Refree
        fields = '__all__'

class CoachSerializer(serializers.ModelSerializer):
    CertificationFile = serializers.FileField()

    class Meta:
        model = Coach
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    CertificationFile = serializers.FileField()

    class Meta:
        model = AdminOfClub
        fields = '__all__'