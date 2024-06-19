from django.shortcuts import render
from rest_framework.views import APIView

from useraccount.models import CustomUser, Account
from transaction.models import Transactions
# Create your views here.

class UserProfileVIew(APIView):
    def get():
        pass