# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-22 19:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outpatients', '0009_auto_20170722_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicationreminder',
            old_name='user',
            new_name='pcc',
        ),
    ]
