# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presence', '0004_auto_20161103_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='checkout',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='session',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
