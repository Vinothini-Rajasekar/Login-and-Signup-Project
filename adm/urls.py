from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('sign_up', signup,name='signup'),
    path('sign_in', signin,name='signin'),
    path('welcome', welcome,name='welcome')

    
    
]