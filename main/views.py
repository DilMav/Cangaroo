from django.shortcuts import render
from . import forms


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def cabinet(request):
    return render(request, 'main/cabinet.html')
