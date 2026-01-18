from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Tasks
from .forms import CreateTask, CreateProject

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
    return render(request, 'projects/projects.html',{
        'projects' : proy
    })

def tasks(request):
    tareas = Tasks.objects.all()
    return render(request, 'tasks/tasks.html',{
        'Tareas': tareas
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html',{
            'form': CreateTask
        })
    else:
        Tasks.objects.create(title = request.POST['title'],description = request.POST['description'], cantidad = request.POST['cantidad'], project_id = 2) #project = Project.objects.get(id=2)
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html',{
            'forms': CreateProject
        })
    else:
        Project.objects.create(name = request.POST['name'],description = request.POST['description'])
        return redirect('projects')
        
