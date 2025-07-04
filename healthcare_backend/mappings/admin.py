from django.contrib import admin
from .models import PatientDoctorMapping

@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'assigned_by', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__first_name', 'doctor__last_name')
    ordering = ('-created_at',)