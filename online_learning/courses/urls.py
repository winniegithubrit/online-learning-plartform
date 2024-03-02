from django.urls import path
from . import views
from .views import home

urlpatterns = [
  
    path('', views.home, name='home'),
    # path('users/', views.user_list, name='user_list'),
    # # those are the names of the views in the views.py page
    # path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    # path('profiles/<int:user_id>/', views.profile_detail, name='profile_detail'),
    # path('courses/', views.course_list, name='course_list'),
    # path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    # path('instructors/', views.instructor_list, name='instructor_list'),
    # path('instructors/<int:instructor_id>/', views.instructor_detail, name='instructor_detail'),
    # path('enrollments/', views.course_enrolled_list, name='course_enrolled_list'),
    # path('enrollments/<int:course_enrolled_id>/', views.course_enrolled_detail, name='course_enrolled_detail'),
    # path('modules/', views.module_list, name='module_list'),
    # path('modules/<int:module_id>/', views.module_detail, name='module_detail'),
]