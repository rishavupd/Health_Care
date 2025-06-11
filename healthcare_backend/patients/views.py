from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Patient
from .serializers import PatientSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return only patients created by the authenticated user
        return Patient.objects.filter(user=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users can only access their own patients
        return Patient.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Patient deleted successfully"},
            status=status.HTTP_200_OK
        )