from django import http
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

#from django.http import HttpResponse
# Create your views here.
def home(requst):
   
    return render(requst, 'users/home.html')

def register(request):
    if request.method == "POST":
     form = UserCreationForm()
     if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         messages.success(request, f'Namastey {username},your account was created succesfully')
         return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html' ,{'form':form})

def profile(request):
    return render(request, 'users/profile.html')