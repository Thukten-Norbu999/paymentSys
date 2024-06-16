from django.urls import path, include
from .views import update_profile_view, view_profile, loginUser, logoutUser, signup, settingsView, home

urlpatterns = [
    path('', home, name='home'),
    path('profile/', view_profile, name='viewProfile' ),
    path('settings/', settingsView, name='settings'),
    path('login/', loginUser, name='loginUser'),
    path('register/', signup, name='signup'),
    path('logout/', logoutUser, name='logout')


]