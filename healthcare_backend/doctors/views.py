from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # All authenticated users can see all doctors
        return Doctor.objects.all()

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        # Only the user who created the doctor can delete it
        if instance.user != request.user:
            return Response(
                {"error": "You don't have permission to delete this doctor"},
                status=status.HTTP_403_FORBIDDEN
            )
        self.perform_destroy(instance)
        return Response(
            {"message": "Doctor deleted successfully"},
            status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # Only the user who created the doctor can update it
        if instance.user != request.user:
            return Response(
                {"error": "You don't have permission to update this doctor"},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().update(request, *args, **kwargs)