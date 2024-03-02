from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader


def home(request):
  template = loader.get_template('courses/home.html')
  return HttpResponse(template.render())

# Create your views here.
