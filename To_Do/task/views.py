from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Task

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'task/task.html', {'task':task})
    
def taskList (request):
    tasks = Task.objects.all()
    return render(request, 'task/list.html', {'tasks': tasks})

def helloWorld (request):
    return HttpResponse('Hello World!!!')

def yourName(request, name):
    return render(request, 'task/yourname.html',{'name':name})
