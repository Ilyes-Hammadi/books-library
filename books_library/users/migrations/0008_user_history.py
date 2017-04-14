# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 04:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0008_auto_20170414_0456'),
        ('users', '0007_remove_user_follwers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='history',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='navigation.History'),
        ),
    ]