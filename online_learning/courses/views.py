from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from django.template import TemplateDoesNotExist
from django.http import HttpResponseServerError


def home(request):
  template = loader.get_template('courses/home.html')
  return HttpResponse(template.render())

def adminDesign(request):
    try:
        return render(request, 'courses/adminDesign.html')
    except TemplateDoesNotExist:
        return HttpResponseServerError('Template not found: adminDesign.html')


