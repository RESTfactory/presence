# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_place_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='code',
            field=models.CharField(default=1, max_length=40, unique=True),
            preserve_default=False,
        ),
    ]