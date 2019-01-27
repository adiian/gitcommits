from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')
    #return HttpResponse('<h1>Hello World</h1>')

def about(request):
    return render(request, 'pages/about.html')