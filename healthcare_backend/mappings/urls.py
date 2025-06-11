from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),
    path('<int:pk>/', views.PatientDoctorMappingDeleteView.as_view(), name='mapping-delete'),
    path('patient/<int:patient_id>/', views.PatientDoctorsByPatientView.as_view(), name='patient-doctors'),
]