from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Warden', 'Warden'),
        ('Student', 'Student'),
        ('Parent','Parent')
    ]
    user_role = models.CharField(max_length = 10, choices=ROLE_CHOICES)
