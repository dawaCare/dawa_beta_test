from __future__ import unicode_literals

from django.db import models

# Create your models here

class Country(models.Model):
    country = models.CharField(max_length=70)

    class Meta:
        db_table = 'countries'

    def __str__(self):
        return self.country

class City(models.Model):
    city = models.CharField(max_length=70)
    country = models.ForeignKey(Country)
    # updated_at = models.DateTimeField()

    class Meta:
        db_table = 'cities'

    def __str__(self):
        return self.city

class Quarter(models.Model):
    quarter = models.CharField(max_length=70)

    class Meta:
        db_table = 'quarters'

    def __str__(self):
        return self.quarter

class Address(models.Model):
    address1 = models.CharField("Address Line 1", max_length=1024)
    address2 = models.CharField("Address Line 2", max_length=1024, null=True, blank=True)
    district = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    city = models.ForeignKey(City)
    quarter = models.ForeignKey(Quarter)

    def __str__(self):
        return self.address1

    class Meta:
        db_table = 'addresses'



# class CountryCode(models.Model):
#     name = models.CharField(max_length=100)
#     code = models.CharField(max_length=2, unique=True)
#
#     def __unicode__(self):
#         return u'%s - %s' % (self.name, self.code)
#
# class AddressModelMixin(models.Model):
#     address1 = models.CharField("Address Line 1"), max_length=1024)
#
#     class Meta:
#         abstract = True
#
# class CameroonAddress(models.Model):
#     address1 = models.CharField("Address Line 1", max_length=1024)
#     address2 = models.CharField("Address Line 2", max_length=1024)
