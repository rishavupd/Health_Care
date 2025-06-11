from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'gender', 'user')
    list_filter = ('gender', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    ordering = ('-created_at',)