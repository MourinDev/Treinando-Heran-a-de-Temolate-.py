from django.shortcuts import render
from django.http import HttpResponse

def home (request):
  return render(request, "tarefas/home.html")

def add_task(request):
    return render(request, "tarefas/adicionar.html")

