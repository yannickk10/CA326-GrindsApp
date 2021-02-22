from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)
