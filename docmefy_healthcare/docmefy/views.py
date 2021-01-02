from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    UpdateView,
    CreateView
)
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from users.models import PatientProfile, DoctorProfile

# Create your views here.

User = get_user_model


class HomePageView(TemplateView):
    template_name = "home.html"
