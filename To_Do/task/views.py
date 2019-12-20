from django.shortcuts import render
from django.http import HttpResponse

def helloWorld (request):
    return HttpResponse('Hello World!!!')

def taskList (request):
    return render(request, 'task/list.html')

def yourName(request, name):
    return render(request, 'task/yourname.html',{'name':name})