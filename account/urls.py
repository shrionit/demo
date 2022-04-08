from django.contrib import admin
from django.urls import path
from account.views import login_view, logout_view, register_view
urlpatterns = [
    path('login', login_view, name="Login"),
    path('logout', logout_view, name="Logout"),
    path('register', register_view, name="Register")
]
