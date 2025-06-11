from django.db import models
from django.conf import settings

class Doctor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctors_created')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    years_of_experience = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialization}"