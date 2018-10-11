from django.http import JsonResponse

from ubereats_app.models import Restaurant
from ubereats_app.serializers import RestaurantSerializer


def customer_get_restaurants(request):
    restaurants = RestaurantSerializer(
        Restaurant.objects.all().order_by('-id'),
        many=True,
        context={"request": request}
    ).data

    return JsonResponse({'restaurants': restaurants})
