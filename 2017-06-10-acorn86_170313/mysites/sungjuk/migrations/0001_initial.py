# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sungjuk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('kor', models.IntegerField()),
                ('eng', models.IntegerField()),
                ('mat', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'sungjuk',
                'verbose_name_plural': 'sungjuks',
            },
        ),
    ]