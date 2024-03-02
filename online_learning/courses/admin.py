from django.contrib import admin

# Register your models here.

from .models import User,Profile,Course,Instructor,Lesson,CourseEnrolled,Module,Quiz,Submission,ProgressTracking


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(CourseEnrolled)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Submission)
admin.site.register(ProgressTracking)