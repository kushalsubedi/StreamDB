from django.db import models
from authentication.models import OurUser
# Create your models here.


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(OurUser, on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now=True)
    flag = models.CharField(max_length=100)

    def __str__(self):
        return self.question


class TermsAndConditions(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
