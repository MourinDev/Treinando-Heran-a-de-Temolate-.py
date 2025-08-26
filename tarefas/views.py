from django.shortcuts import render
from django.http import HttpResponse

def home (request):
  return render(request, "tarefas/home.html")

def add_task(request):
    task = "New Task"
    return HttpResponse(task)


