from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import OurUserManager


class OurUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    # streamger_id = models.AutoField(unique=True, primary_key=True)
    created_by = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # flag = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['streamger_id']

    objects = OurUserManager()

    def __str__(self):
        return self.email


class Customer(models.Model):
    # Add fields for Customer
    user = models.OneToOneField(
        OurUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name
