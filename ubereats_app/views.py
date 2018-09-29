from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    return redirect(restaurant_home)


def restaurant_sign_up(request):
    return render(request, 'restaurant/sign-up.html', {})


@login_required(login_url='/restaurant/sign-in/')
def restaurant_home(request):
    return render(request, 'restaurant/home.html', {})
