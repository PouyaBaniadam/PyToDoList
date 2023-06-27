from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('completed', 'completed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=40, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    time = models.TimeField(blank=False, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=False, null=False, default="pending")
