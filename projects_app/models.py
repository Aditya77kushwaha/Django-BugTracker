from django.db import models
from django import forms
from django.utils.timezone import now
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="projects",null=True)
    name = models.CharField(max_length=50)
    organization_name = models.CharField(max_length=70)
    technology = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(default=now)
    def __str__(self):
        return self.name