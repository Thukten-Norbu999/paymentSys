from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from .models import CustomUser, Account
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
def checkLegal(dob):
        age = relativedelta(date.today(), datetime.strptime(dob, "%Y-%m-%d").date())
        return age.years >= 18

@login_required()
def view_profile(request):
    user = request.user

    if user.is_authenticated:
        email = user.objects.email
        phoneNo = user.phoneNo

    return render(request, 'profile/viewProfile.html')


@login_required()
def update_profile_view(request):
    pass


def loginUser(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        if email and password:
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                
                login(request, user)
                messages.success(request,'Login Successful')
                return redirect('viewProfile')
            else:
                
                messages.error(request, 'Wrong Credentials. Try again')
        else:
            
            messages.error(request, 'Please Enter The Details')
    return render(request, 'auth/login.html')

@login_required()
def logoutUser(request):
    user = request.user

    if user.is_authenticated:
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

        age = checkLegal(dob=dob)
        if age:
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
                        account = Account.objects.create(user=user)
                        
                        user.save()
                        account.save()
                        return redirect('home')
                else:
                    messages.error(request, "User already exist")
        else:
            messages.error(request, "The applicant should be 18 and above")
    return render(request, 'auth/signup.html', )