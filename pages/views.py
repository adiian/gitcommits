from django.shortcuts import render
from django.http import HttpResponse

from projects.models import Project

def index(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'pages/index.html', context)
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')