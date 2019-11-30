from django.db import models 

class CityWeather(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    temperature = models.CharField(max_length=5)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)