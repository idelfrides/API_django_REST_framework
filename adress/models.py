from django.db import models


class Adress(models.Model):
    line1 = models.CharField(max_length=150)
    line2 = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.line1
