from django import forms
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from .models import CustomUser, PatientProfile

# Write your code here.

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class PatientCreationForm(forms.ModelForm):

    email = forms.EmailField(max_length=255, label='Email', required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta():
        model = PatientProfile
        fields = ('email', 'full_name', 'age', 'mobile')

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use.")

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, request, *args, **kwargs):
        email = self.cleaned_data["email"].lower()
        password1 = self.cleaned_data["password1"]
        full_name = self.cleaned_data["full_name"]
        age = self.cleaned_data["age"]
        mobile = self.cleaned_data["mobile"]
        user = User.objects.create_patient(email=email, password=password1)
        patientProfile = PatientProfile(
            patient=user, full_name=full_name, age=age, mobile=mobile)
        patientProfile.save()
        return user
