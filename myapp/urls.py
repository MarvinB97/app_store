from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/',views.about),
    path('project/<int:id>', views.projects),
    path('tasks/<int:id>',views.tasks),
    path('hello/<str:username>', views.hello)
]