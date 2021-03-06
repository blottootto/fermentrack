# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-04 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gravity', '0004_ispindel_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ispindelconfiguration',
            name='constant_term',
            field=models.FloatField(default=0.0, help_text='The constant term in the gravity conversion equation'),
        ),
        migrations.AlterField(
            model_name='ispindelconfiguration',
            name='first_degree_coefficient',
            field=models.FloatField(default=0.0, help_text='The first degree coefficient in the gravity conversion equation'),
        ),
        migrations.AlterField(
            model_name='ispindelconfiguration',
            name='second_degree_coefficient',
            field=models.FloatField(default=0.0, help_text='The second degree coefficient in the gravity conversion equation'),
        ),
        migrations.AlterField(
            model_name='ispindelconfiguration',
            name='third_degree_coefficient',
            field=models.FloatField(default=0.0, help_text='The third degree coefficient in the gravity conversion equation'),
        ),
    ]
