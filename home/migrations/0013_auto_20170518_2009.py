# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-18 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20170518_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, default='', null=True, to='home.Tag'),
        ),
    ]
