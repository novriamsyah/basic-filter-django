from django.contrib import admin
from .models import *

class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotelName', 'bannerImage', 'hotelPrice']
    

admin.site.register(Amenities)
admin.site.register(Hotel)
admin.site.register(HotelImage)
