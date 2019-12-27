from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import TaskForm

from .models import Task

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:        
        form = TaskForm()
        return render(request,'task/addtask.html', {'form':form})

def editTask(request, id):
    task = get_object_or_404(Task, pk =id)
    form = TaskForm(instance=task)

    if (request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'task/edittask.html', {'form':form, 'task':task})
    else:
        return render(request, 'task/edittask.html', {'form':form, 'task':task})

def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('/')

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'task/task.html', {'task':task})
    
def taskList (request):
    tasks = Task.objects.all().order_by('-created_at') #atualizar
    return render(request, 'task/list.html', {'tasks': tasks})

def helloWorld (request):
    return HttpResponse('Hello World!!!')

def yourName(request, name):
    return render(request, 'task/yourname.html',{'name':name})
