# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 04:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0007_auto_20170414_0450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookhistory',
            name='user',
        ),
        migrations.RemoveField(
            model_name='search',
            name='user',
        ),
    ]
