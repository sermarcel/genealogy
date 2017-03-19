# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-18 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genealogy_app', '0003_auto_20170220_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='relation_name',
            field=models.IntegerField(choices=[(-1, 'nie określono'), (0, 'syn'), (1, 'córka'), (2, 'ojciec'), (3, 'matka'), (4, 'brat'), (5, 'siostra'), (6, 'partner')], default=-1),
        ),
    ]
