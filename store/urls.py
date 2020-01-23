from django.conf.urls import url
from django.urls import path
from .views import HomePageView, AboutPageView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView



urlpatterns = [
    path('Biographie.html',AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),   

]


def home(request):
    return HttpResponse('index.html'),

def about(request):
    return HttpResponse('Biographie.html'),
