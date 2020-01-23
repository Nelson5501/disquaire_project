from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import admin


class HomePageView(TemplateView): 
    template_name = 'index.html'


class AboutPageView(TemplateView): 
    template_name = 'about.html'

