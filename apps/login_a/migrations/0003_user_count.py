# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_a', '0002_user_highfives'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
