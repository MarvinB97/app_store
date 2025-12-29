from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Tasks

# Create your views here.

def index(request):
    return HttpResponse('<h2>Index page</h2>')

def hello(request, username):
    return HttpResponse("Hello %s" % username)

def about(request):
    return HttpResponse("<h1>About</h1>")

def projects(request, id):
    proy = Project.objects.get(id = id)
    return HttpResponse("<h1>Proyecto:</h1>" \
    "<p>%s</p>" % proy.name)

def tasks(request, id):
    tarea = Tasks.objects.get(id=id)
    return HttpResponse("<h1>Tarea:</h1>" \
    "<p>%s</p>" % tarea.title)