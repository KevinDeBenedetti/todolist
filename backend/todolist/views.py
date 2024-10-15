from django.shortcuts import render
from .models import Task
from .filters import TaskFilter
from django.core.paginator import Paginator
# home/
from django.shortcuts import render
# api/
from rest_framework import viewsets
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import JSONRenderer
# swagger/
from django.views.decorators.csrf import csrf_exempt # Désactiver la protection CSRF sur les API
from django.utils.decorators import method_decorator
from todolist.permissions import HasValidAPIToken

# home/
def home(request):
    return render(request, 'home.html')

# tasks/
@csrf_exempt
def task_list(request):
    task_filter = TaskFilter(request.GET, queryset=Task.objects.all().order_by('due_date'))
    paginator = Paginator(task_filter.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'task_list.html', {'filter': task_filter, 'page_obj': page_obj})

# api/
@method_decorator(csrf_exempt, name='dispatch')
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('due_date')
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completed', 'assigned_to']
    renderer_classes = [JSONRenderer]
    permission_classes = [HasValidAPIToken]