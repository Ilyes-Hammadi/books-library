# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-07 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recomendation', '0002_recommender_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommender',
            name='name',
            field=models.CharField(default='my-recommender', max_length=120, unique=True),
        ),
    ]
