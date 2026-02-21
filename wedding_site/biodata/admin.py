from django.contrib import admin
from .models import CommunityBiodata

@admin.register(CommunityBiodata)
class CommunityBiodataAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'full_name', 'gotra', 'deity_number', 'contact_display')
    search_fields = ('full_name', 'serial_number', 'gotra')

    def contact_display(self, obj):
        # This mimics the "Contact Admin" logic for the list view
        return "Contact Admin"
    contact_display.short_description = "Mobile"