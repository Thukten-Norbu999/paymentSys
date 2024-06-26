from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from .models import CustomUser, Account
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from django.http import Http404
from django.db import IntegrityError


# from .decorator import unauthenticated_user, checkAccountExistent

def checkLegal(dob):
        age = relativedelta(date.today(), datetime.strptime(dob, "%Y-%m-%d").date())
        return age.years >= 18

def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login/')
def settingsView(request):
    return render(request, 'profile/settings.html')

@login_required(login_url='/login/')
def view_profile(request):
    try:
        # Retrieve the current user's CustomUser object
        user = CustomUser.objects.get(email=request.user.email)
        account = Account.objects.get(user=user)
    except Account.DoesNotExist:
        try:
            account = Account.objects.create(user=request.user)
            account.save()
        except IntegrityError:
            pass
        # Handle the case where the user doesn't exist (optional)
        

    user = request.user
    account = Account.objects.get(user=user)
    # Access user attributes directly
    email = user.email
    phoneNo = user.phoneNo
    dob = date.isoformat(user.dob)
    qr_url = account.get_qr_url(account)+"{}".format(account.qrcode())
    # print(type(dob))
    content = {
        'email': email, 
        'phoneNo': phoneNo, 
        'dob':dob, 
        'account':account,
        'qrurl': qr_url
    }
    return render(request, 'profile/viewProfile.html', content)

@login_required(login_url='/login/')
def update_profile_view(request):
    pass


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('viewProfile')
    else:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]

                
            user = authenticate(request, email=email, password=password)
            check = CustomUser.objects.filter(email=email)
            if check:

            
                if user is not None:
                    
                    login(request, user)
                    messages.success(request,'Login Successful')
                    return redirect('home')
                else:
                    
                    messages.error(request, 'Wrong Credentials. Try again with correct credentials')
            else:
                messages.error(request, 'User Does Not Exist')
            
            
        return render(request, 'auth/login.html')
    

@login_required(login_url='/login/')
def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('loginUser')


def signup(request):
    if request.user.is_authenticated:
        return redirect('viewProfile')
    else:
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
                    user = CustomUser.objects.filter(email=email)
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
                            login(request,user)
                            return redirect('home')
                    else:
                        messages.error(request, "User already exist")
            else:
                messages.error(request, "The applicant should be 18 and above")
        return render(request, 'auth/signup.html', )