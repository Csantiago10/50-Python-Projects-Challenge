from django.contrib import admin
from core.models import Profile 

@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    # Add a list display for the 'name', 'role', and 'skills' fields
    list_display = ('name', 'role', 'skills')
    # Add a search bar for the 'name' and 'role' fields
    search_fields = ('name', 'role')
    # Add a filter for the 'role' field
    list_filter = ('role',)

