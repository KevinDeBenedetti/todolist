from django.db import models
from django.contrib.auth.models import User

# Tâche
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField()
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
# Token
class APIToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)  # Facultatif, pour une description du token
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token