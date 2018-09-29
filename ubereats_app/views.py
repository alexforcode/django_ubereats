from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ubereats_app.forms import RestaurantForm, UserForm


def index(request):
    return redirect(restaurant_home)


def restaurant_sign_up(request):
    user_form = UserForm()
    restaurant_form = RestaurantForm()

    return render(request,
                  'restaurant/sign-up.html',
                  {'user_form': user_form,
                   'restaurant_form': restaurant_form})


@login_required(login_url='/restaurant/sign-in/')
def restaurant_home(request):
    return render(request, 'restaurant/home.html', {})
