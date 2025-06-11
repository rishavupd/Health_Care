from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']

    def validate_email(self, value):
        if self.instance:
            if Patient.objects.filter(email=value).exclude(pk=self.instance.pk).exists():
                raise serializers.ValidationError("Patient with this email already exists.")
        else:
            if Patient.objects.filter(email=value).exists():
                raise serializers.ValidationError("Patient with this email already exists.")
        return value