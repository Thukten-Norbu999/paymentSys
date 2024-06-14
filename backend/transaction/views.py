from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


@login_required
def payment(request):
    user = request.user

@login_required
def viewHistory(request):
    user = request.user


