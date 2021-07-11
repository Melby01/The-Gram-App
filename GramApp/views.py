from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def login(request):
    context = {}
    return render(request, 'all-gram//login.html', context)

def register(request):
    context = {}
    return render(request, 'all-gram/register.html', context)