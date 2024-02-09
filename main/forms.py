from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.conf import settings


class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "password1", "password2")

    email = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder": "Your Email"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Your Password"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Repeat Password"})
    )


class EditUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "password1", "password2")

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your First name"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your Last name"})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder": "Your Email"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Your Password"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Repeat Password"})
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your Email"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Your Password"})
    )
