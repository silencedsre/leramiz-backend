from django.db import models
from django.urls import reverse
from django.utils.timezone import datetime
# Create your models here.

class FeaturedListing(models.Model):
    #key features
    street_address  =  models.CharField(max_length=200, null=True)
    location        =  models.CharField(max_length=200, null=True)
    area            =  models.PositiveIntegerField(null=True)
    bedrooms        =  models.PositiveIntegerField(null=True)
    agent_name      =  models.CharField(max_length=200)
    garages         =  models.PositiveIntegerField(null=True)
    bathroom        = models.PositiveIntegerField(null=True)
    timestamp       =  models.DateTimeField(default=datetime.now())
    price           =  models.PositiveIntegerField(null=True)
    featured        =  models.BooleanField(default=False)
    sale_rent       =  models.BooleanField(default=True)
    image           = models.ImageField(upload_to="img/feature")

    #extra fields for detail view
    image1 = models.ImageField(upload_to="img/feature/detail", null=True)
    image2 = models.ImageField(upload_to="img/feature/detail", null=True)
    image3 = models.ImageField(upload_to="img/feature/detail", null=True)
    image4 = models.ImageField(upload_to="img/feature/detail", null=True)

    #extra features
    building_type = models.CharField(max_length=200, null=True)
    build_age    = models.PositiveIntegerField(default=1)

    #description
    description = models.TextField(blank=True)

    #properties detail
    air_conditioning  = models.BooleanField(default=True)
    telephone = models.BooleanField(default=True)
    laundry_room = models.BooleanField(default=True)
    central_heating = models.BooleanField(default=True)
    # building_type = models.ForeignKey()
    metro_central = models.BooleanField(default=True)
    city_views = models.BooleanField(default=True)
    internet  = models.BooleanField(default=True)
    electric_range = models.BooleanField(default=True)

    def __str__(self):
        return self.street_address

    def get_absolute_url(self):
        return reverse(viewname='featured_listing:detail', kwargs={'pk':self.pk})
