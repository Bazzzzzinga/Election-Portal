# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-07 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Election_Portal', '0010_remove_candidate_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='vote_count',
            field=models.IntegerField(default=0),
        ),
    ]
