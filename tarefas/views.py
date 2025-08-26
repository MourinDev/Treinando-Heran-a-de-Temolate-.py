from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    frase = "Hello, world! This is my first Django app."
    return HttpResponse(frase)
def add_task(request):
    task = "New Task"
    return HttpResponse(task)


