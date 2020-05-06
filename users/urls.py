from django.contrib import admin
from django.urls import path
from . import views

app_name = "users"

# as this is family matter, I do not allow creating users.

urlpatterns = [
    path('login/', views.login_user, name="login_user"),
    path('logout/', views.logout_user, name="logout_user"),
]
