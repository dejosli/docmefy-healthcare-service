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
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import PatientProfile, DoctorProfile

# Create your views here.

User = get_user_model


@login_required
def profile_redirect_view(request):
    user = request.user
    if user.is_patient:
        user_id = user.id
        patient_profile = get_object_or_404(PatientProfile, pk=user_id)
        return render(request, 'patient-profile.html', {'profile': patient_profile})

    if user.is_doctor:
        user_id = user.id
        doctor_profile = get_object_or_404(DoctorProfile, pk=user_id)
        return render(request, 'doctor-profile.html', {'profile': doctor_profile})

    if user.is_superuser:
        return redirect('/admin/')

    # return HttpResponseRedirect(reverse('account_signup'))
