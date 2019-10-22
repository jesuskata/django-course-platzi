"""Posts Models."""

# Django
from django.db import models

class User(models.Model):
    """User Model."""
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
