# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-18 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genealogy_app', '0002_auto_20170218_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anceator',
            name='maiden_name',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
        migrations.AlterField(
            model_name='anceator',
            name='secound_name',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
