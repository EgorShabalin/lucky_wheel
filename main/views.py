import random

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from main.models import Wheel, Profile
from .forms import SignupForm, EditUserForm
from django.contrib.auth import get_user_model
from custom_user.models import User


def index(request):
    return render(request, "index.html", {})


def wheel(request):
    usr = Profile.objects.get(current_user=request.user)
    wheel = Wheel
    wheel_list = wheel.wheel_list
    percentage = wheel.percentage

    balance = 0

    def spin(wheel_list, percentage, balance):
        new_wheel = []
        for w, p in zip(wheel_list, percentage):
            new_wheel.extend(p * [w])
        attempt = random.choice(new_wheel)
        if attempt.isdigit():
            balance += int(attempt)
            balance = balance - 5
            usr.balance += balance
            usr.save()
        if attempt == "tripple":
            balance = usr.balance * 3
            balance = balance - 5
            usr.balance = 0
            usr.balance += balance
            usr.save()
        if attempt == "double":
            balance = usr.balance * 2
            balance = balance - 5
            usr.balance = 0
            usr.balance += balance
            usr.save()
        if attempt == "jackpot":
            balance += 2000
            balance = balance - 5
            usr.balance += balance
            usr.save()
        if attempt == "broke":
            balance = 0
            usr.balance = 0
            usr.save()
        return [attempt, balance]

    result = spin(wheel_list, percentage, balance)

    prize = result[0]

    remain = usr.balance

    return render(
        request,
        "wheel.html",
        {
            "wheel_list": wheel_list,
            "percentage": percentage,
            "remain": remain,
            "prize": prize,
        },
    )


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("/")

    else:
        form = SignupForm()

    return render(request, "main/signup.html", {"form": form})
