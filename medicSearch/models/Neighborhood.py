from django.db import models
from medicSearch.models import City

class Neighborhood(models.Model):
    city = models.ForeignKey(City, null=True, related_name='city', on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.city.name}'