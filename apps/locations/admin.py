from django.contrib import admin
from apps.locations.models import Address, City, Country, Quarter
# Register your models here.

admin.site.register(Address)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Quarter)
