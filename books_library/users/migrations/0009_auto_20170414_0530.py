# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 05:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='history',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='navigation.History'),
        ),
    ]