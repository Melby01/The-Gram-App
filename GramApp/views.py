from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to The Instagram App')

def login(request):
    context = {}
    return render(request, 'all-gram//login.html', context)