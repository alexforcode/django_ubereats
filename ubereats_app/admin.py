from django.contrib import admin

from ubereats_app.models import Restaurant, Customer, Driver, Meal, Order, OrderDetails


admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(OrderDetails)
