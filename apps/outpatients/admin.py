from django.contrib import admin
from apps.outpatients.models import Outpatient, EmergencyContact, MedicationCategory, Medication, PrescribedMed, Diagnosis, DiagnosisCategories, Visit, Allergy, Appointment, Facility, Department, Doctor, Specialty, Certification, AppointmentReminder, MedicationReminder, PatientCareCoordinator, Comment
from django.contrib.contenttypes.admin import GenericStackedInline


# Register your models here.
# class OutpatientResource(ModelResource):
#
#     class Meta:
#         model = Outpatient

# class OutpatientAdmin(admin.ModelAdmin):
    # resource_class = OutpatientResource

class CommentInline(GenericStackedInline):
    model = Comment
    ct_field = "content_type"
    ct_fk_field = "object_id"
    fk_name = "content_object"
    extra = 0

class AppointmentAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

class PrescribedMedAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Outpatient)
admin.site.register(EmergencyContact)
admin.site.register(MedicationCategory)
admin.site.register(Medication)
admin.site.register(PrescribedMed, PrescribedMedAdmin)
admin.site.register(Diagnosis)
admin.site.register(DiagnosisCategories)
admin.site.register(Visit)
admin.site.register(Allergy)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Facility)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Specialty)
admin.site.register(Certification)
admin.site.register(AppointmentReminder)
admin.site.register(MedicationReminder)
admin.site.register(PatientCareCoordinator)
admin.site.register(Comment)
