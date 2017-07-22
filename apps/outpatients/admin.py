from django.contrib import admin
from apps.outpatients.models import Outpatient, EmergencyContact, MedicationCategory, Medication, PrescribedMed, Diagnosis, DiagnosisCategories, Visit, Allergy, Appointment, Facility, Department, Doctor, Specialty, Certification, AppointmentReminder, MedicationReminder, Comment
from django.contrib.contenttypes.admin import GenericStackedInline
import nested_admin


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

class AppointmentInline(admin.TabularInline):
    model = Appointment

# class PrescribedMedInline(admin.TabularInline):
#     model = PrescribedMed

class MedicationReminderInline(nested_admin.NestedTabularInline):
    model = MedicationReminder
    sortable_field_name = "id"

class PrescribedMedInline(nested_admin.NestedTabularInline):
    model = PrescribedMed
    sortable_field_name = "id"
    inlines = [
        MedicationReminderInline
    ]

# class OutpatientAdmin(admin.ModelAdmin):
#     inlines = [
#         AppointmentInline,
#         PrescribedMedInline,
#     ]

class EmergencyContactInline(nested_admin.NestedTabularInline):
    model = EmergencyContact

class VisitInline(nested_admin.NestedTabularInline):
    model = Visit

class AppointmentReminderInline(nested_admin.NestedTabularInline):
    model = AppointmentReminder

class AppointmentInline(nested_admin.NestedTabularInline):
    model = Appointment
    sortable_field_name = "id"
    inlines = [
        AppointmentReminderInline
    ]


class OutpatientAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        PrescribedMedInline,
        EmergencyContactInline,
        VisitInline,
        AppointmentInline,
    ]
    list_display = ('last_name', 'first_name', 'date_of_birth', 'address', 'get_diagnoses', 'get_meds')
    search_fields = ['last_name', 'first_name']

admin.site.register(Outpatient, OutpatientAdmin)
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
# admin.site.register(PatientCareCoordinator)
admin.site.register(Comment)
