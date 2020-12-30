from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_patient = models.BooleanField(default=False, verbose_name='Patient', help_text='Designates whether this user should be treated as patient.')
    is_doctor = models.BooleanField(default=False, verbose_name='Doctor', help_text='Designates whether this user should be treated as doctor.')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class PatientProfile(models.Model):
    patient = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=150)
    age = models.IntegerField()
    # email = models.EmailField(max_length=150, unique=True)
    mobile = models.CharField(max_length=12)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.patient.email


class DoctorProfile(models.Model):
    doctor = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=50)
    university = models.CharField(max_length=150)
    licence = models.CharField(max_length=25)
    # email = models.EmailField(max_length=150, unique=True)
    mobile = models.CharField(max_length=12)

    def __str__(self):
        return self.doctor.email
