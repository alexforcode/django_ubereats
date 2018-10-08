from django.contrib import admin

from ubereats_app.models import Restaurant, Customer, Driver, Meal


admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Meal)
