from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .models import  Image,Profile,Comment
from .forms import NewPostForm ,ProfileForm,NewsLetterForm,CommentForm,Registration
from django.contrib import messages

@login_required(login_url='/accounts/login/')
def index(request):
    date = dt.date.today()
    images = Image.objects.all()
    current_user = request.user
    users = Profile.objects.all()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email = email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('index')
    else:
        form = NewsLetterForm()
    return render(request, 'all-gram/index.html', {"date": date,"images":images, "users":users, "form": form})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.Author = current_user
            post.save()
        return redirect('new-post')
    else:
        form = NewPostForm()
    return render(request, 'all-gram/post.html', {"form": form})

 
def convert_dates(dates):
    
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_insta(request,past_date):
    try:
    # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Insta for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    if date == dt.date.today():
        return redirect(news_of_day)    
    return render(request, 'all-gram/past-gram.html', {"date": date})

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'images/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gram/search.html',{"message":message})


@login_required(login_url='/accounts/login/')  
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('instaToday')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = current_user
            post.save()
        return redirect('instaToday')
    else:
        form = CommentForm()
    return render(request, 'new_comment.html', {"form": form})
 
def register(request):
    if request.method == 'POST':
     form = Registration(request.POST)
     if form.is_valid():
      form.save()
      email = form.cleaned_data['email']
      username = form.cleaned_data.get('username')

      messages.success(request,f'Account for {username} created,you can now login')
      return redirect('login')
    else:
      form = Registration()
    return render(request,'registration/registration_form.html',{"form":form})