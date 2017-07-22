from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from apps.locations.models import Address
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class Specialty(models.Model):
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'specialties'

class Certification(models.Model):
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'certifications'

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    main_phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.ForeignKey(Address)

    certifications = models.ManyToManyField(Certification)
    specialties = models.ManyToManyField(Specialty)

    class Meta:
        db_table = 'doctors'

class Department(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'departments'


class Facility(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.ForeignKey(Address)
    departments = models.ManyToManyField(Department)

    class Meta:
        db_table = 'facilities'

class Allergy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = 'allergies'

class MedicationCategory(models.Model):
    category = models.CharField(max_length=50)

    class Meta:
        db_table = 'medication_categories'


class DiagnosisCategories(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'diagnosis_categories'

class Diagnosis(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(DiagnosisCategories)

    class Meta:
        db_table = 'diagnoses'


class Medication(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    medication_category = models.ForeignKey(MedicationCategory)

    # prescribers = models.ManyToManyField(Outpatient, through='PrescribedMed')

    class Meta:
        db_table = 'medications'

class Outpatient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField("Date of Birth")
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # international country number
    idd = models.PositiveIntegerField(default=237)
    main_phone = models.CharField(max_length=10)
    alt_phone = models.CharField(max_length=10, null=True)
    occupation = models.CharField(max_length=30, null=True)
    address = models.ForeignKey(Address)

    pregnant = models.NullBooleanField()
    signed_consent_for_roi = models.BooleanField(default=True)
    reason_for_not_signing_consent = models.TextField(null=True)
    admitted = models.NullBooleanField()
    consultation_fee = models.FloatField()
    has_all_prescribed_medications = models.BooleanField()
    issues_with_taking_medicatin = models.BooleanField()

    diagnoses = models.ManyToManyField(Diagnosis)
    allergies = models.ManyToManyField(Allergy)
    medications = models.ManyToManyField(Medication, through="PrescribedMed")

    def get_diagnoses(self):
        return self.diagnoses.all()

    def get_meds(self):
        return self.medications.all()
    #
    # def get_visits(self):
    #     return self.visits.all()

    class Meta:
        db_table = 'outpatients'


class EmergencyContact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    main_phone = models.CharField(max_length=10)
    alt_phone = models.CharField(max_length=10, null=True)
    RELATIONSHIP_CHOICES = (
        ('Sib', 'Sibling'),
        ('M', 'Mother'),
        ('F', 'Father'),
        ('C', 'Cousin'),
    )
    relationship = models.CharField(max_length=10, choices=RELATIONSHIP_CHOICES)
    address = models.ForeignKey(Address)
    outpatient = models.ForeignKey(Outpatient)



    class Meta:
        db_table = 'emergency_contacts'


class PrescribedMed(models.Model):
    medication = models.ForeignKey(Medication, related_name='prescription')
    outpatient = models.ForeignKey(Outpatient, related_name='prescription')
    dosage_num = models.IntegerField()
    route = models.CharField(max_length=10)
    frequency = models.CharField(max_length=10)
    dosage_unit = models.CharField(max_length=10)

    class Meta:
        db_table = 'prescribedmeds'

class Visit(models.Model):
    visit_date = models.DateTimeField()
    doctors_note = models.TextField()
    patient_received_ed = models.BooleanField()
    lab_fee = models.FloatField()

    outpatient = models.ForeignKey(Outpatient)
    doctor = models.ForeignKey(Doctor)
    facility = models.ForeignKey(Facility)

    class Meta:
        db_table = 'visits'

class Appointment(models.Model):
    appt_date = models.DateTimeField()

    facility = models.ForeignKey(Facility)
    doctor = models.ForeignKey(Doctor)
    outpatient = models.ForeignKey(Outpatient)
    department = models.ForeignKey(Department)
    visit = models.ForeignKey(Visit)

    followed_up = models.BooleanField(default=False)



    class Meta:
        db_table = 'appointments'



class MedicationReminder(models.Model):
    prescribed_med = models.ForeignKey(PrescribedMed)
    pcc = models.ForeignKey(User, null=True)

    contacted_patient = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    message = models.TextField()

    date = models.DateTimeField()



    class Meta:
        db_table = 'med_reminders'

class AppointmentReminder(models.Model):
    appt_date = models.ForeignKey(Appointment)
    pcc = models.ForeignKey(User)

    contacted_patient = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    message = models.TextField()

    date = models.DateTimeField()



    class Meta:
        db_table = 'appt_reminders'


class Comment(models.Model):
    comment = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


# class TrackedModel(models.Model):
#     # these fields are set automatically from REST requests via
#     # updates from dict and the getter, setter properties, where available
#     # (from the update from dict mixin)
#     created = models.DateTimeField(blank=True, null=True)
#     updated = models.DateTimeField(blank=True, null=True)
#     created_by = models.ForeignKey(
#         User, blank=True, null=True,
#         # related_name="created_%(app_label)s_%(class)s_subrecords"
#     )
#     updated_by = models.ForeignKey(
#         User, blank=True, null=True,
#         # related_name="updated_%(app_label)s_%(class)s_subrecords"
#     )
#
#     class Meta:
#         abstract = True
#
#     def set_created_by_id(self, incoming_value, user, *args, **kwargs):
#         if not self.id:
#             # this means if a record is not created by the api, it will not
#             # have a created by id
#             self.created_by = user
#
#     def set_updated_by_id(self, incoming_value, user, *args, **kwargs):
#         if self.id:
#             self.updated_by = user
#
#     def set_updated(self, incoming_value, user, *args, **kwargs):
#         if self.id:
#             self.updated = timezone.now()
#
#     def set_created(self, incoming_value, user, *args, **kwargs):
#         if not self.id:
#             # this means if a record is not created by the api, it will not
#             # have a created timestamp
#
#             self.created = timezone.now()
