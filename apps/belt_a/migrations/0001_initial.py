# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_a', '0004_auto_20170928_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gave', to='login_a.User')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received', to='login_a.User')),
            ],
        ),
    ]