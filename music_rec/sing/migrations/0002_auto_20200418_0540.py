# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-18 05:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='singinfo',
            old_name='title',
            new_name='name',
        ),
    ]
