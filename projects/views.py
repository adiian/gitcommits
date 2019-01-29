from django.shortcuts import render

from .models import Project
# Create your views here.
# fix VS error https://stackoverflow.com/questions/45135263/class-has-no-objects-member
def index(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'projects/projects.html', context)

def project(request):
    return render(request, 'projects/project.html')

def search(request):
    return render(request, 'projects/search.html')    