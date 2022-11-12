from django.db import models


class Amenities(models.Model):
    amenity = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.amenity
    
class Hotel(models.Model):
    hotelName = models.CharField(max_length= 200)
    hotelPrice = models.IntegerField()
    amenities = models.ManyToManyField(Amenities)
    bannerImage = models.ImageField(upload_to="hotels")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.hotelName
    
    def get_amenities(self):
        payload = []
        
        for amenity in self.amenities.all():
            payload.append({'id':amenity.id, 'amenity':amenity.amenity})
        return payload

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="hotels")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.hotel.hotelName
    
