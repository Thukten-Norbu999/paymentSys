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
            messages.error(request, 'Wrong Credentials')
    else:
        return render(request, 'auth/login.html',{

        })

@login_required()
def logoutUser(request):
    user = request.user

    if user:
        logout()

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        fName = request.POST['firstName']
        lName = request.POST['lastName']
        phoneNo = request.POST['phoneNo']
        pw = request.POST['pw']
        cpw = request.POST['cpw']
        gender = request.POST['gender']
        dob = request.POST['dob']

        if cpw != pw:
            messages.error(request,"The passwords does not match")
        else:
            user = CustomUser.objects.filter(email=email, password=cpw)
            if not user:
                if fName and lName and email and cpw:
                    user = CustomUser.objects.create_user(
                        
                        email=email,
                        first_name=fName, 
                        last_name=lName,
                        phoneNo=phoneNo,
                        gender=gender,
                        dob=dob,
                        password=cpw,
                        )
                    user.save()
                    return redirect('home')
            else:
                messages.error(request, "User already exist")
    return render(request, 'auth/signup.html', )