from django import forms
from .models import OtpCode
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegisterForm(forms.Form):
    username    = forms.CharField(max_length=255)
    email    = forms.EmailField(max_length=255)
    #phone    = forms.CharField(max_length=11)
    password = forms.CharField(label='password',widget=forms.PasswordInput)

    def clean_email(self):
        """checking uniqeness of email"""
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError("This email is already exists")
        return email

        
        