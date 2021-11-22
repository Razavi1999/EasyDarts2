from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Account

import Account
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length = 254 ,
                             help_text = 'Required. Add a valid email address.'
                             )
    class Meta:
        model = Account
        fields = ('email' , 'username' , 'password1' , 'password2')

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget = forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email' , 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleande_data['password']
            if not authenticate(email=email , password = password):
                return forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email' , 'username')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = Account.objects.get(email=email)

        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        OurUsername = self.cleaned_data['username']
        try:
            Account.objects.get(username=OurUsername)

        except Account.DoesNotExist:
            return OurUsername
        raise forms.ValidationError('Username "%s" is already in use.' % OurUsername)