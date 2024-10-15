from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

# View to render the HTML page
def index(request):
    return render(request, 'index.html')  

# API ViewSet to perform CRUD operations on tasks
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
