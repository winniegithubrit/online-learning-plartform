from django.shortcuts import render
from .models import *

from django.http import HttpResponse
from django.template import loader



def home(request):
  template = loader.get_template('courses/home.html')
  return HttpResponse(template.render())

def adminDesign(request):
  template = loader.get_template('courses/adminDesign.html')
  return HttpResponse(template.render())

def simple(request):
  template = loader.get_template('courses/simple.html')
  return HttpResponse(template.render())


