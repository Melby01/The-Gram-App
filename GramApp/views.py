from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def login(request):
    context = {}
    return render(request, 'all-gram//login.html', context)

def register(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'all-gram/register.html', context)

def search_results(request):
    
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_user = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-gram/search.html',{"message":message,"user": searched_user})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gram/search.html',{"message":message})