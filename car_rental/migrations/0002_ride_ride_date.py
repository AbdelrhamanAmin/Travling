# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-21 18:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='Ride_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 21, 18, 47, 23, 216758)),
        ),
    ]