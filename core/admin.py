from django.contrib import admin
from .models import TouristSpot


class TouristSpotModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'adress', 'update']
    list_filter= ['name', 'evaluation', 'aproved']
    list_display_links = ['update']
    list_editable = ['name']
    search_fields = ['name', 'evaluation', 'aproved']

    class Meta:
        model = TouristSpot


# Register your models here.
admin.site.register(TouristSpot, TouristSpotModelAdmin)
