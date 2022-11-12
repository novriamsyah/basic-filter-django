from django.shortcuts import render
from .models import *
from django.http import JsonResponse


def Home(request):
    context = {'amenities' : Amenities.objects.all()}
    return render(request, 'home.html', context)

def get_hotel(request):
    try:
        hotel_objs = Hotel.objects.all()
        
        if request.GET.get('sort_by'):
            sort_by_value = request.GET.get('sort_by')
            if sort_by_value == 'asc':
                hotel_objs = hotel_objs.order_by('hotelPrice')
            elif sort_by_value == 'dsc':
                hotel_objs = hotel_objs.order_by('-hotelPrice')
        
        if request.GET.get('amount'):
            amount = request.GET.get('amount')
            hotel_objs = hotel_objs.filter(hotelPrice__lte = amount)
            
        if request.GET.get('amenities'):
            amenities = request.GET.get('amenities')
            amenities = str(amenities).split(',')
            am = []
            
            for amenity in amenities:
                am.append(int(amenity))
            print(am)
            hotel_objs = hotel_objs.filter(amenities__in = am).distinct()
        
        payload = []
        
        for hotel_obj in hotel_objs:
            payload.append({
                'hotelName' : hotel_obj.hotelName,
                'hotelPrice' : hotel_obj.hotelPrice,
                'bannerImage' : '/media/' + str(hotel_obj.bannerImage),
                'amenities' : hotel_obj.get_amenities(),
            })
        return JsonResponse(payload, safe=False)
        
    except Exception as e:
        print(e)
    
    return JsonResponse({'massage': 'terjadi kesalahan'})
