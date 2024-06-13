from django.shortcuts import render
from .models import Task



def index(request):
    tasks = Task.objects.order_by('-id')[:3]
    return render(request, 'main/index.html', {'tasks': tasks})


def about(request):
    tasks = Task.objects.order_by('-id')[:10]
    return render(request, 'main/about.html', {'tasks': tasks})


def contacts(request):

    return render(request, 'main/contacts.html')


def enter(request):
    return render(request, 'main/enter.html')


