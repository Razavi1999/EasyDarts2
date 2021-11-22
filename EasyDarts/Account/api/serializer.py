from rest_framework import serializers

from Account.models import *


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type' : 'password'},
        write_only=True
    )

    class Meta:
        model = Account
        fields = ['first_name' , 'last_name' , 'email' , 'nick_name','phone_number' , 'role','password']

    def save(self, **kwargs):
        role = ''
        if 'role' not in self.validated_data:
            role = 'normal-user'

        nick_name = ''
        if 'nick_name' not in self.validated_data:
            nick_name = 'Darts Guy'

        account = Account(
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            phone_number=self.validated_data['phone_number'],
            role = role,
            nick_name = nick_name
        )

        password = self.validated_data['password']

        account.set_password(self.validated_data['password'])
        account.save()
        return account



class AccountPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'user_id', 'first_name', 'last_name', 'email', 'phone_number',
            'gender', 'national_code', 'image', 'role', 'bio', 'birthday', 'currency'
        ]

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'