from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from apps.locations.models import Address
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class Demographics(PatientSubrecord):
    _is_singleton = True
    _icon = 'fa fa-user'

    # hospital_number = models.CharField(
    #     max_length=255, blank=True,
    # -    help_text=b("The unique identifier for this patient at the hospital.")
    # )
    # nhs_number = models.CharField(
    #     max_length=255, blank=True, null=True, verbose_name=b("NHS Number")
    # )

    surname = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    title = ForeignKeyOrFreeText(Title)
    date_of_birth = models.DateField(
        null=True, blank=True, verbose_name=b("Date of Birth")
    )
    marital_status = ForeignKeyOrFreeText(MaritalStatus)
    religion = models.CharField(max_length=255, blank=True, null=True)
    date_of_death = models.DateField(
        null=True, blank=True, verbose_name=b("Date of Death")
    )
    post_code = models.CharField(max_length=20, blank=True, null=True)
    gp_practice_code = models.CharField(
        max_length=20, blank=True, null=True,
        verbose_name=b("GP Practice Code")
    )
    # birth_place = ForeignKeyOrFreeText(Destination,
    #                                    verbose_name=b("Country of Birth"))
    ethnicity = ForeignKeyOrFreeText(Ethnicity)
    death_indicator = models.BooleanField(
        default=False,
        help_text=b("This field will be True if the patient is deceased.")
    )

    sex = ForeignKeyOrFreeText(Gender)

    @property
    def name(self):
        return '{0} {1}'.format(self.first_name, self.surname)

    class Meta:
        abstract = True


class Patient(models.Model):

    # objects = managers.PatientQueryset.as_manager()

    def __unicode__(self):
        try:
            demographics = self.demographics_set.get()
            return '%s | %s %s' % (
                demographics.hospital_number,
                demographics.first_name,
                demographics.surname
            )
        except models.ObjectDoesNotExist:
            return 'Patient {0}'.format(self.id)
        except:
            print(self.id)
            raise

    def create_episode(self, **kwargs):
        return self.episode_set.create(**kwargs)

    def get_active_episode(self):
        for episode in self.episode_set.order_by('id').reverse():
            if episode.active:
                return episode
        return None

    # @transaction.atomic()
    # def bulk_update(self, dict_of_list_of_upgrades, user,
    #                 episode=None, force=False):
    #     """
    #             takes in a dictionary of api name to a list of fields and
    #             creates the required subrecords. If passed an episode
    #             sub record but no episode it will create an episode
    #             and attatch it.
    #
    #             e.g. {"allergies": [
    #                         {"drug": "paracetomol"}
    #                         {"drug": "aspirin"}
    #                       ],
    #                   "investigation":[
    #                         {"name": "some test", "details": "some details"}
    #                       ]
    #                  }
    #     """
    #     if "demographics" not in dict_of_list_of_upgrades:
    #         if not self.id:
    #             dict_of_list_of_upgrades["demographics"] = [{}]
    #
    #     if not self.id:
    #         self.save()
    #
    #     #
    #     # We never want to be in the position where we don't have an episode.
    #     # If this patient has never had an episode, we create one now.
    #     # If the patient has preexisting episodes, we will either use an
    #     # episode passed in to us as a kwarg, or create a fresh episode for
    #     # this bulk update once we're sure we have episode subrecord data to
    #     # save.
    #     #
    #     if not self.episode_set.exists():
    #         episode = self.create_episode()
    #
    #     for api_name, list_of_upgrades in dict_of_list_of_upgrades.items():
    #
    #         # for the moment we'll ignore tagging as it's weird
    #         if(api_name == "tagging"):
    #             continue
    #         model = get_subrecord_from_api_name(api_name=api_name)
    #         if model in episode_subrecords():
    #             if episode is None:
    #                 episode = self.create_episode(patient=self)
    #                 episode.save()
    #
    #             model.bulk_update_from_dicts(episode, list_of_upgrades, user,
    #                                          force=force)
    #         else:
    #             # it's a patient subrecord
    #             model.bulk_update_from_dicts(self, list_of_upgrades, user,
    #                                          force=force)
    # #
    # def to_dict(self, user):
    #     active_episode = self.get_active_episode()
    #     d = {
    #         'id': self.id,
    #         'episodes': {episode.id: episode.to_dict(user) for episode in
    #                      self.episode_set.all()},
    #         'active_episode_id': active_episode.id if active_episode else None,
    #     }
    #
    #     for model in patient_subrecords():
    #         subrecords = model.objects.filter(patient_id=self.id)
    #         d[model.get_api_name()] = [
    #             subrecord.to_dict(user) for subrecord in subrecords
    #         ]
    #     return d

    # def update_from_demographics_dict(self, demographics_data, user):
    #     demographics = self.demographics_set.get()
    #     demographics.update_from_dict(demographics_data, user)
    #
    # def save(self, *args, **kwargs):
    #     created = not bool(self.id)
    #     super(Patient, self).save(*args, **kwargs)
    #     if created:
    #         for subclass in patient_subrecords():
    #             if subclass._is_singleton:
    #                 subclass.objects.create(patient=self)
