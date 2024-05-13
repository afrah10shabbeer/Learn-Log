"""Defines URL patterns for accounts"""

from django.urls import path, include
from . import views
app_name = 'accounts'
urlpatterns = [
    # Include default auth urls from django
    path('',include('django.contrib.auth.urls')), # login page URL pattern matches the 
                                                # http://localhost:8000/accounts/login/
    
    # Registration page
    path('register/',views.register,name='register'),
]
