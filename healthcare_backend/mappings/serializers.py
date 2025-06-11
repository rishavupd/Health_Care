from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    assigned_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'assigned_by', 'reason_for_visit',
                 'patient_details', 'doctor_details', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'assigned_by']

    def validate(self, data):
        if self.instance is None:
            if PatientDoctorMapping.objects.filter(
                patient=data.get('patient'),
                doctor=data.get('doctor')
            ).exists():
                raise serializers.ValidationError("This patient is already assigned to this doctor.")
        return data