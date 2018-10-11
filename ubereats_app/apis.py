from django.http import JsonResponse

from ubereats_app.models import Restaurant, Meal
from ubereats_app.serializers import RestaurantSerializer, MealsSerializer


def customer_get_restaurants(request):
    restaurants = RestaurantSerializer(
        Restaurant.objects.all().order_by('-id'),
        many=True,
        context={"request": request}
    ).data

    return JsonResponse({'restaurants': restaurants})


def customer_get_meals(request, restaurant_id):
    meals = MealsSerializer(
        Meal.objects.filter(restaurant_id=restaurant_id).order_by('-id'),
        many=True,
        context={'request': request}
    ).data

    return JsonResponse({'meals': meals})


def customer_add_order(request):
    return JsonResponse({})


def customer_get_latest_order(request):
    return JsonResponse({})
