import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            'title': ['icontains'],
            'assigned_to': ['exact'],
            'completed': ['exact'],
            'due_date': ['gte', 'lte'],
            'priority': ['exact', 'gte', 'lte'],
        }