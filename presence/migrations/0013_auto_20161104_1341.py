# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_remove_place_pois'),
        ('presence', '0012_auto_20161104_0306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='entity',
        ),
        migrations.AddField(
            model_name='session',
            name='place',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='places.Place'),
            preserve_default=False,
        ),
    ]
