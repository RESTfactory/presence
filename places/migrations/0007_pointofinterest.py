# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-12 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20161007_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_id', models.IntegerField(blank=True, editable=False, unique=True)),
                ('address', models.CharField(blank=True, editable=False, max_length=255)),
                ('latitude', models.CharField(blank=True, max_length=30)),
                ('longitude', models.CharField(blank=True, max_length=30)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
