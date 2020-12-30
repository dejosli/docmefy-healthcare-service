from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models import fields
from allauth.account.forms import SignupForm

from .models import CustomUser, PatientProfile

# Write your code here.


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
