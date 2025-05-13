from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Only required for migrations, can be empty


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.full_name} ({self.email})"