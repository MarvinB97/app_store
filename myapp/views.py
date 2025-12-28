from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h2>Index page</h2>')

def hello(request, username):
    return HttpResponse("Hello %s" % username)

def about(request):
    return HttpResponse("<h1>About</h1>")