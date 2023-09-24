from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    
    if request.method=="POST" :   
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Successfully Create for {username}!')  
            return redirect("user-register")  
    else:
        form = RegisterForm()
    return render(request,"users/register.html",{"form": form})
# Create your views here.
def home(request):
    return render(request,"users/home.html")