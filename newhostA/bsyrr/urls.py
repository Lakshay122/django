from atexit import register
from django.urls import path, include

from bsyrr.views import UserRegistrationView

urlpatterns = [

    path('register/', UserRegistrationView.as_view(), name='register')
]
