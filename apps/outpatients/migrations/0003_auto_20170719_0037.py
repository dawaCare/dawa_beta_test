# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-19 00:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outpatients', '0002_auto_20170719_0037'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='medicationcategory',
            table='medication_categories',
        ),
    ]
