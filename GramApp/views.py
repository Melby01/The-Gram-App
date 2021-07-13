from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import *
from django.views.generic import ListView,DetailView
from django.template import RequestContext
import datetime as dt
from . forms import NewsLetterForm,NewPostForm
from . email import send_welcome_email
from .forms import *


# Create your views here.

    
@login_required(login_url='/accounts/login/')    
def profile(request):
    if request.method == 'POST':

        userForm = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if  profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('home')

    else:
        
        profile_form = ProfileUpdateForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)

        params = {
            'user_form':user_form,
            'profile_form': profile_form

        }

    return render(request, 'all-ig/profile.html', params)

def prof(request):
    # user_prof = get_object_or_404(User, username=username)
    # if request.user == user_prof:
    #     return redirect('profile', username=request.user.username)
    profile = Profile.objects.filter(user = request.user)
    return render(request,"all-ig/profile.html",{"profile":profile})


def editProfile(request):
    
    if request.method == 'POST':

        userForm = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if  profile_form.is_valid():
            userForm.save()
            profile_form.save()

            return redirect('profile')

    else:
        
        profile_form = ProfileUpdateForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)

        params = {
            'user_form':user_form,
            'profile_form': profile_form

        }

    return render(request, 'all-ig/updateProfile.html', params)


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
    return render(request, 'all-ig/index.html', {"date": date,"images":images, "users":users, "form": form})

def search_results(request):
    '''
    Method to search by location or category
    '''
    if 'result' in request.GET and request.GET["result"]:
        search_term = request.GET.get("result")
        searched_images = Image.search_by_author(search_term)
       
        message = f"{search_term}"
        return render(request, 'all-ig/search.html', {"message":message, "images":searched_images})
    elif 'result' in request.GET and request.GET["result"]:
        search_term = request.GET.get("result")
        searched_images = .search_by_author(search_term)
        message = f"{search_term}"    

        return render(request, 'all-ig/search.html', {"message":message, "images":searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-ig/search.html', {"message":message})

    
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = current_user
            post.save()
        return redirect('post')
    else:
        form = NewPostForm()
    return render(request, 'all-ig/post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def comment(request,id):
    current_user = request.user
    image = get_object_or_404(Post, id=id)
    comment = Comments.objects.filter(image = id).all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.user = current_user
            comment.image = image
            comment.save()
            return redirect('/')
    else:
        form = CommentForm()
    return render(request,'comment.html',{"form":form, "comment": comment})


@login_required(login_url='/accounts/login/')
def newPost(request):
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)        
        if form.is_valid():
            image=form.cleaned_data.get('image')
            imageCaption=form.cleaned_data.get('imageCaption')
            post = Image(image = image,imageCaption= imageCaption, profile=user_profile)
            post.savePost()
            
        else:
            print(form.errors)

        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'newPost.html', {"form": form})
