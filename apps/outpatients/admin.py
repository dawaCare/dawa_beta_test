from django.contrib import admin
from apps.outpatients.models import Outpatient, EmergencyContact, MedicationCategory, Medication, PrescribedMed

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
