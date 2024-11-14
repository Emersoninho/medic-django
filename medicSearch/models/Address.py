from django.db import models
from medicSearch.models import Neighborhood, Dayweek

class Address(models.Model):
    neighborhood = models.ForeignKey(Neighborhood, null=True, related_name='Neighborhood', on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=255, null=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    longitude = models.DecimalField(max_digits=9, decimal_places=7)
    opening_time =models.TimeField()
    closing_time = models.TimeField()
    day_week = models.ManyToManyField(Dayweek, blank=True, related_name='day_week')
    phone = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100, null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name