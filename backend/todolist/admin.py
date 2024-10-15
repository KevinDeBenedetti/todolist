from django.contrib import admin
from .models import Task, APIToken

# Tâches
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'completed', 'due_date', 'assigned_to' ,'created_at', 'updated_at')
    list_filter = ('completed', 'due_date', 'priority', 'assigned_to')
    search_fields = ('title', 'description')

# Token d'accès à l'API
@admin.register(APIToken)
class APITokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'description', 'created_at')
    search_fields = ('token', 'description')