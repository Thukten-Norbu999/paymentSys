from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from .models import CustomUser

@login_required()
def view_profile(request):
    pass

@login_required()
def update_profile_view(request):
    pass


def loginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        pw = request.POST['password']

        user = authenticate(email, pw)
        if user:
            messages.success(request, 'Login Successful')
        else:
            pass
    else:
        return render(request, 'auth/login.html',{

        })

@login_required()
def logoutUser(request):
    user = request.user

    if user:
        logout()

def signup(request):
    pass