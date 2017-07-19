from django.contrib import admin
from apps.outpatients.models import Outpatient, EmergencyContact, MedicationCategory, Medication, PrescribedMed, Diagnosis, DiagnosisCategories, Visit, Allergy, Appointment, Facility, Department, Doctor, Specialty, Certification, AppointmentReminder, MedicationReminder, PatientCareCoordinator, Comment

# Register your models here.
# class OutpatientResource(ModelResource):
#
#     class Meta:
#         model = Outpatient

# class OutpatientAdmin(admin.ModelAdmin):
    # resource_class = OutpatientResource

admin.site.register(Outpatient)
admin.site.register(EmergencyContact)
admin.site.register(MedicationCategory)
admin.site.register(Medication)
admin.site.register(PrescribedMed)
admin.site.register(Diagnosis)
admin.site.register(DiagnosisCategories)
admin.site.register(Visit)
admin.site.register(Allergy)
admin.site.register(Appointment)
admin.site.register(Facility)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Specialty)
admin.site.register(Certification)
admin.site.register(AppointmentReminder)
admin.site.register(MedicationReminder)
admin.site.register(PatientCareCoordinator)
admin.site.register(Comment)
