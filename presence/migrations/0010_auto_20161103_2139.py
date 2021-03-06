# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 21:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presence', '0009_session_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='session',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='presence.Session'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checkout',
            name='session',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='presence.Session'),
            preserve_default=False,
        ),
    ]
