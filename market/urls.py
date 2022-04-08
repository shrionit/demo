from django.contrib import admin
from django.urls import path
from market.views import marketview
urlpatterns = [
    path('', marketview, name="Home"),
]
