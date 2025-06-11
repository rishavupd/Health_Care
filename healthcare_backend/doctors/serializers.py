from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']

    def validate_email(self, value):
        if self.instance:
            if Doctor.objects.filter(email=value).exclude(pk=self.instance.pk).exists():
                raise serializers.ValidationError("Doctor with this email already exists.")
        else:
            if Doctor.objects.filter(email=value).exists():
                raise serializers.ValidationError("Doctor with this email already exists.")
        return value

    def validate_license_number(self, value):
        if self.instance:
            if Doctor.objects.filter(license_number=value).exclude(pk=self.instance.pk).exists():
                raise serializers.ValidationError("Doctor with this license number already exists.")
        else:
            if Doctor.objects.filter(license_number=value).exists():
                raise serializers.ValidationError("Doctor with this license number already exists.")
        return value