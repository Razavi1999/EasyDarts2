from django.urls import path

from Account.api.views import *

urlpatterns = [
    path('register', registration_view, name='register'),
    path('login', TokenObtainView.as_view(), name='login'),
    path('properties/update', update_account_view, name='update'),
]