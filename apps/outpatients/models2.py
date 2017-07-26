from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from apps.locations.models import Address
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class Subrecord(TrackedModel, models.Model):
    # consistency_token = models.CharField(max_length=8)
    _is_singleton = False
    # _advanced_searchable = True
    _exclude_from_subrecords = False

    class Meta:
        abstract = True

    # def __unicode__(self):
    #     if self.created:
    #         return '{0}: {1} {2}'.format(
    #             self.get_api_name(), self.id, self.created
    #         )
    #     else:
    #         return '{0}: {1}'.format(self.get_api_name(), self.id)

    # @classmethod
    # def get_api_name(cls):
    #     return camelcase_to_underscore(cls._meta.object_name)
    #
    # @classmethod
    # def get_icon(cls):
    #     return getattr(cls, '_icon', None)
    #
    # @classmethod
    # def get_display_name(cls):
    #     if hasattr(cls, '_title'):
    #         return cls._title
    #     if cls._meta.verbose_name.islower():
    #         return cls._meta.verbose_name.title()
    #     return cls._meta.verbose_name
    #
    # @classmethod
    # def _get_template(cls, template, prefixes=None):
    #     template_locations = []
    #
    #     if prefixes is None:
    #         prefixes = []
    #
    #     for prefix in prefixes:
    #         template_locations.append(
    #             template.format(os.path.join(prefix, cls.get_api_name()))
    #         )
    #
    #     template_locations.append(template.format(cls.get_api_name()))
    #     return find_template(template_locations)
    #
    # @classmethod
    # def get_display_template(cls, prefixes=None):
    #     """
    #     Return the active display template for our record
    #     """
    #     if prefixes is None:
    #         prefixes = []
    #
    #     return cls._get_template(
    #         os.path.join("records", "{}.html"),
    #         prefixes=prefixes
    #     )
    #
    # @classmethod
    # def get_detail_template(cls, prefixes=None):
    #     """
    #     Return the active detail template for our record
    #     """
    #     file_locations = [
    #         'records/{0}_detail.html',
    #         'records/{0}.html'
    #     ]
    #
    #     if prefixes is None:
    #         prefixes = []
    #
    #     templates = []
    #
    #     for prefix in prefixes:
    #         for file_location in file_locations:
    #             templates.append(file_location.format(
    #                 os.path.join(prefix, cls.get_api_name())
    #             ))
    #
    #     for file_location in file_locations:
    #         templates.append(
    #             file_location.format(cls.get_api_name())
    #         )
    #     return find_template(templates)
    #
    # @classmethod
    # def get_form_template(cls, prefixes=None):
    #     if prefixes is None:
    #         prefixes = []
    #
    #     return cls._get_template(
    #         template=os.path.join("forms", "{}_form.html"),
    #         prefixes=prefixes
    #     )
    #
    # @classmethod
    # def get_form_url(cls):
    #     return reverse("form_view", kwargs=dict(model=cls.get_api_name()))
    #
    # @classmethod
    # def get_modal_template(cls, prefixes=None):
    #     """
    #     Return the active form template for our record
    #     """
    #     if prefixes is None:
    #         prefixes = []
    #
    #     result = cls._get_template(
    #         template=os.path.join("modals", "{}_modal.html"),
    #         prefixes=prefixes
    #     )
    #
    #     if not result and cls.get_form_template():
    #         result = find_template(["base_templates/form_modal_base.html"])
    #
    #     return result
    #
    # @classmethod
    # def bulk_update_from_dicts(
    #     cls, parent, list_of_dicts, user, force=False
    # ):
    #     """
    #         allows the bulk updating of a field for example
    #         [
    #             {"test": "blah 1", "details": "blah blah"}
    #             {"test": "blah 2", "details": "blah blah"}
    #         ]
    #
    #         parent is the parent class, that can be Episode or Patient
    #
    #         this method will not delete. It updates if there's an id or if
    #         the model is a singleton otherwise it creates
    #     """
    #     schema_name = parent.__class__.__name__.lower()
    #
    #     if cls._is_singleton:
    #         if len(list_of_dicts) > 1:
    #             msg = "attempted creation of multiple fields on a singleton {}"
    #             raise ValueError(msg.format(cls.__name__))
    #
    #     result = []
    #
    #     for a_dict in list_of_dicts:
    #         if "id" in a_dict or cls._is_singleton:
    #             if cls._is_singleton:
    #                 query = cls.objects.filter(**{schema_name: parent})
    #                 subrecord = query.get()
    #             else:
    #                 subrecord = cls.objects.get(id=a_dict["id"])
    #         else:
    #             a_dict["{}_id".format(schema_name)] = parent.id
    #             subrecord = cls(**{schema_name: parent})
    #
    #         subrecord.update_from_dict(a_dict, user, force=force)
    #         result.append(subrecord)
    #     return result


class PatientSubrecord(Subrecord):
    patient = models.ForeignKey(Patient)

    class Meta:
        abstract = True


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
    # title = ForeignKeyOrFreeText(Title)
    date_of_birth = models.DateField(
        null=True, blank=True, verbose_name=b("Date of Birth")
    )
    # marital_status = ForeignKeyOrFreeText(MaritalStatus)
    # religion = models.CharField(max_length=255, blank=True, null=True)
    # date_of_death = models.DateField(
    #     null=True, blank=True, verbose_name=b("Date of Death")
    # )
    # post_code = models.CharField(max_length=20, blank=True, null=True)
    # gp_practice_code = models.CharField(
    #     max_length=20, blank=True, null=True,
    #     verbose_name=b("GP Practice Code")
    # )
    # birth_place = ForeignKeyOrFreeText(Destination,
    #                                    verbose_name=b("Country of Birth"))
    # ethnicity = ForeignKeyOrFreeText(Ethnicity)
    # death_indicator = models.BooleanField(
    #     default=False,
    #     help_text=b("This field will be True if the patient is deceased.")
    # )

    # sex = ForeignKeyOrFreeText(Gender)

    @property
    def name(self):
        return '{0} {1}'.format(self.first_name, self.surname)

    class Meta:
        abstract = True

class Episode(TrackedModel):
    """
    An individual episode of care.

    A patient may have many episodes of care, but this maps to one occasion
    on which they found themselves on "The List".
    """
    category_name     = models.CharField(
        max_length=200, default=get_default_episode_type
    )
    patient           = models.ForeignKey(Patient)
    active            = models.BooleanField(default=False)
    date_of_admission = models.DateField(null=True, blank=True)
    # TODO rename to date_of_discharge?
    discharge_date    = models.DateField(null=True, blank=True)
    date_of_episode   = models.DateField(blank=True, null=True)
    consistency_token = models.CharField(max_length=8)

    # stage is at what stage of an episode flow is the
    # patient at
    stage             = models.CharField(
        max_length=256, null=True, blank=True
    )

    objects = managers.EpisodeQueryset.as_manager()


    def save(self, *args, **kwargs):
        created = not bool(self.id)
        super(Episode, self).save(*args, **kwargs)
        if created:
            for subclass in episode_subrecords():
                if subclass._is_singleton:
                    subclass.objects.create(episode=self)

    # @classmethod
    # def _get_fieldnames_to_serialize(cls):
    #     fields = super(Episode, cls)._get_fieldnames_to_serialize()
    #     fields.extend(["start", "end"])
    #     return fields

    @cached_property
    def start(self):
        return self.category.start

    @cached_property
    def end(self):
        return self.category.end

    @property
    def category(self):
        from opal.core import episodes
        category = episodes.EpisodeCategory.get(self.category_name.lower())
        return category(self)

    def visible_to(self, user):
        """
        Predicate function to determine whether this episode is visible to
        a certain user.

        The logic for visibility is held in individual
        opal.core.episodes.EpisodeCategory implementations.
        """
        return self.category.episode_visible_to(self, user)

    # def set_tag_names(self, tag_names, user):
    #     """
    #     1. Set the episode.active status
    #     2. Special case mine
    #     3. Archive dangling tags not in our current list.
    #     4. Add new tags.
    #     5. Ensure that we're setting the parents of child tags
    #     6. There is no step 6.
    #     """
    #     if len(tag_names) and not self.active:
    #         self.active = True
    #         self.save()
    #     elif not len(tag_names) and self.active:
    #         self.active = False
    #         self.save()
    #
    #     if "mine" not in tag_names:
    #         self.tagging_set.filter(user=user,
    #                                 value='mine').update(archived=True)
    #     else:
    #         tag, created = self.tagging_set.get_or_create(
    #             value='mine', user=user
    #         )
    #         if not created:
    #             tag.archived = False
    #             tag.save()
    #
    #         tag_names = [t for t in tag_names if not t == 'mine']
    #
    #     # nuke everything and start from fresh so we don't have
    #     # to deal with childless parents
    #     self.tagging_set.exclude(value="mine").filter(archived=False).update(
    #         archived=True,
    #         updated_by=user,
    #         updated=timezone.now()
    #     )
    #     parents = []
    #     for tag in tag_names:
    #         parent = tagging.parent(tag)
    #         if parent:
    #             parents.append(parent)
    #     tag_names += parents
    #
    #     for tag in tag_names:
    #         tagg, created = self.tagging_set.get_or_create(
    #             value=tag, episode=self
    #         )
    #         if created:
    #             tagg.created_by = user
    #             tagg.created = timezone.now()
    #         else:
    #             tagg.archived = False
    #             tagg.updated_by = user
    #             tagg.updated = timezone.now()
    #
    #         tagg.save()

    # def tagging_dict(self, user):
    #     tag_names = self.get_tag_names(user)
    #     tagging_dict = {i: True for i in tag_names}
    #     tagging_dict["id"] = self.id
    #     return [tagging_dict]
    #
    # def get_tag_names(self, user, historic=False):
    #     """
    #     Return the current active tag names for this Episode as strings.
    #     """
    #     qs = self.tagging_set.filter(Q(user=user) | Q(user=None))
    #     if not historic:
    #         qs = qs.filter(archived=False)
    #
    #     return qs.values_list("value", flat=True)



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

    # def create_episode(self, **kwargs):
    #     return self.episode_set.create(**kwargs)
    #
    # def get_active_episode(self):
    #     for episode in self.episode_set.order_by('id').reverse():
    #         if episode.active:
    #             return episode
    #     return None



class TrackedModel(models.Model):
    # these fields are set automatically from REST requests via
    # updates from dict and the getter, setter properties, where available
    # (from the update from dict mixin)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, blank=True, null=True,
        related_name="created_%(app_label)s_%(class)s_subrecords"
    )
    updated_by = models.ForeignKey(
        User, blank=True, null=True,
        related_name="updated_%(app_label)s_%(class)s_subrecords"
    )

    class Meta:
        abstract = True

    def set_created_by_id(self, incoming_value, user, *args, **kwargs):
        if not self.id:
            # this means if a record is not created by the api, it will not
            # have a created by id
            self.created_by = user

    def set_updated_by_id(self, incoming_value, user, *args, **kwargs):
        if self.id:
            self.updated_by = user

    def set_updated(self, incoming_value, user, *args, **kwargs):
        if self.id:
            self.updated = timezone.now()

    def set_created(self, incoming_value, user, *args, **kwargs):
        if not self.id:
            # this means if a record is not created by the api, it will not
            # have a created timestamp

            self.created = timezone.now()
