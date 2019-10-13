from django.contrib import admin
from .models import Attraction

class AttractionModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'description','opening_hours', 'minimum_age']
    list_editable = ['minimum_age']
    list_filter = ['name', 'minimum_age']
    search_fields = ['minimum_age', 'name']

    class Meta:
        model = Attraction



admin.site.register(Attraction, AttractionModelAdmin)

