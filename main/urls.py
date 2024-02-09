from django.urls import path
from main.views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout as auth_logout
from .forms import LoginForm


app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path("wheel/", wheel, name="wheel"),
    path("signup/", signup, name="signup"),
    path(
        "user_login/",
        auth_views.LoginView.as_view(
            template_name="main/login.html", authentication_form=LoginForm
        ),
        name="user_login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
]
