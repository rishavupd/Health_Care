from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer
from patients.models import Patient

class PatientDoctorMappingListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users can see all mappings for their patients
        return PatientDoctorMapping.objects.filter(
            patient__user=self.request.user
        )

class PatientDoctorMappingDeleteView(generics.DestroyAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            assigned_by=self.request.user
        )

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Mapping deleted successfully"},
            status=status.HTTP_200_OK
        )

class PatientDoctorsByPatientView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, patient_id):
        # Check if patient exists and belongs to the user
        patient = get_object_or_404(
            Patient, 
            id=patient_id, 
            user=request.user
        )
        
        mappings = PatientDoctorMapping.objects.filter(patient=patient)
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        
        return Response({
            'patient': {
                'id': patient.id,
                'name': f"{patient.first_name} {patient.last_name}"
            },
            'mappings': serializer.data
        })