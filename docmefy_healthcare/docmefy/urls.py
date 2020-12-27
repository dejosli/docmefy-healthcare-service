from django.urls import path

from docmefy import views

urlpatterns = [
    path('', views.home, name='home'),
]