from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login,logout


def register(request):
    if request.method== "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            auth_login(request, user)
            return redirect("posts:blog") 
    else:
        form = UserCreationForm()  

    return render(request, "users/register.html", {"form": form})




def login_view(request):
    
    if request.method == "POST":
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            user = form.get_user() 
            auth_login(request, user)
            return redirect("posts:blog")
     
    else:
        form = AuthenticationForm()  

    return render(request, "users/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("users:login")
