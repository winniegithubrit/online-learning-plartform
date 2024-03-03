from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adminDesign/', views.adminDesign, name='adminDesign'),  # Add this line
    # Other URL patterns...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Only needed for development
