# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marcador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='date_created',
            field=models.DateTimeField(auto_now=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='date updated'),
        ),
    ]
