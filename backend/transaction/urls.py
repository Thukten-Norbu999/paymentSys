from django.urls import path, include
# from .views import update_profile_view, view_profile, loginUser, logoutUser
from .views import viewHistory, payment

urlpatterns = [
    path('history/', viewHistory, name='viewHistory'),
    path('payment/', payment, name='payment')
]