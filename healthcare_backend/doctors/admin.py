from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'license_number', 'email')
    list_filter = ('specialization', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'license_number')
    ordering = ('-created_at',)