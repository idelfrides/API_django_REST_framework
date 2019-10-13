from django.contrib import admin
from .models import Adress

class AdressModelAdmin(admin.ModelAdmin):
    list_display = ['line1', 'city', 'state', 'country', 'update']
    list_filter= ['city', 'state']
    list_display_links = ['update']
    list_editable = ['line1']
    search_fields = ['city', 'state']

    class Meta:
        model = Adress  

        

admin.site.register(Adress, AdressModelAdmin)

