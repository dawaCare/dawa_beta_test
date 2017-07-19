from django.contrib import admin
from apps.locations.models import Address, City, Country
# Register your models here.

admin.site.register(Address)
admin.site.register(City)
admin.site.register(Country)
