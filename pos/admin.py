from django.contrib import admin

from pos.models import Order, Receipt

# Register your models here.
admin.site.register(Order)

admin.site.register(Receipt)
