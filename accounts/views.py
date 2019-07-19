from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisierForm, UserLoginForm
from django.contrib.auth.models import User
from django.views.generic import (
            TemplateView,
            ListView,
            DetailView,
            CreateView,
            UpdateView,
            DeleteView,
            FormView
)

# Create your views here.
def index(request):
    return render(request, "index.html")

def register_user(request):
    form = UserRegisierForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.create_user(username, email, password)
        if user is not None:
            return redirect('/login')
    return render(request, "register.html", {'form':form})

def login_user(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("Login Failed")
    return render(request, "login.html", {'form':form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('/')