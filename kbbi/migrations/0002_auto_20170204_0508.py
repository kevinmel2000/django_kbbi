# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-04 05:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbbi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kbbidata',
            name='id',
        ),
        migrations.AddField(
            model_name='kbbidata',
            name='_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
