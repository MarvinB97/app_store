from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Tasks

# Create your views here.

def index(request):
    list = [1,2,3]
    return render(request, 'index.html',{
        'lista':list
    })

def hello(request, username):
    return HttpResponse("Hello %s" % username)

def about(request):
    return render(request, 'about.html')

def projects(request):
    proy = Project.objects.all()
    return render(request, 'projects.html',{
        'projects' : proy
    })

def tasks(request, id):
    tarea = Tasks.objects.get(id=id)
    return HttpResponse("<h1>Tarea:</h1>" \
    "<p>%s</p>" % tarea.title)