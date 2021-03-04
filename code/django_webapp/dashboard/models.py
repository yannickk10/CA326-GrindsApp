from django.contrib.auth.models import AbstractUser
from django.db import models
from quiz.models import User, Subject, Student


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ManyToManyField(User, related_name='members')
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name
