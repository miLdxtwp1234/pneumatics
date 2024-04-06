from django.db import models

class Role(models.Model):
    TEACHER = '1'
    STUDENT = '2'

    ROLE_CHOICES = [
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    ]

    role_id = models.CharField(max_length=100, choices=ROLE_CHOICES, primary_key=True)
    role_name = models.CharField(max_length=100)

class ReportScore(models.Model):
    student = models.OneToOneField('Student', on_delete=models.CASCADE, primary_key=True)
    pre_test = models.IntegerField(null=True)
    post_test = models.IntegerField(null=True)

class Student(models.Model):
    student_id = models.CharField(max_length=255, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  
    token = models.CharField(max_length=2555, null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
