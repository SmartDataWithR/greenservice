import pandas as pd
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm

class DataView(ListView):
    template_name = "home.html"

    def get_query(self):
        return 



def home(request):
    template = "home.html"
    return render(request, template, {})
   

def about(request):
    from pages.namer import namer
    return render(request, "about.html", {"my_stuff": namer()})

def contact(request):
    return render(request, "contact.html", {})    

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have successfully logged in.'))
            return redirect('home')
        else:
            messages.success(request, ('You failed to login.'))
            return redirect('login_user')

    else:
        return render(request, "authenticate/login_user.html", {})    

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out.'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have registered.'))
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'authenticate/register.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save() 
            messages.success(request, ('You have edited your profile.'))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'authenticate/edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save() 
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You have edited your password.'))
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'authenticate/change_password.html', context)