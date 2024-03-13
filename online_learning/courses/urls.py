from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('adminDesign/', views.adminDesign, name='adminDesign'), 
    path('simple/', views.simple, name='simple'), 

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
