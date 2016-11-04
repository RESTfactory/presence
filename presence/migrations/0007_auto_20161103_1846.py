# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presence', '0006_auto_20161103_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkin',
            name='session',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='session',
        ),
        migrations.AlterField(
            model_name='session',
            name='end',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='start',
            field=models.DateTimeField(blank=True),
        ),
    ]
