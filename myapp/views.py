from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Tasks

# Create your views here.

def index(request):
    return render(request, 'index.html')

def hello(request, username):
    return HttpResponse("Hello %s" % username)

def about(request):
    return render(request, 'about.html')

def projects(request, id):
    proy = Project.objects.get(id = id)
    return HttpResponse("<h1>Proyecto:</h1>" \
    "<p>%s</p>" % proy.name)

def tasks(request, id):
    tarea = Tasks.objects.get(id=id)
    return HttpResponse("<h1>Tarea:</h1>" \
    "<p>%s</p>" % tarea.title)