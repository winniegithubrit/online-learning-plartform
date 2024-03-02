from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(blank=True, null=True)
    date_of_birth = models.DateField()
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True, blank=True)
    duration = models.CharField(max_length=50)
    difficulty_level = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    prerequisites = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return self.title

class Instructor(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

class CourseEnrolled(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField()
    progress = models.CharField(max_length=255)

    def __str__(self):
        return str(self.course)


class Module(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Quiz(models.Model):
    text = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)  
    options = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_submissions')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answers = models.TextField() 
    timestamp = models.DateTimeField(auto_now_add=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

class ProgressTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress_trackings')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)
    progress_percentage = models.IntegerField(default=0) 
