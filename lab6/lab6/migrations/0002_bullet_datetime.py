# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab7', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bullet',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
