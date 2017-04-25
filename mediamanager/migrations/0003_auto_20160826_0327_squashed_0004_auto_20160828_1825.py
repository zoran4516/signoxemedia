# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 10:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    replaces = [('mediamanager', '0003_auto_20160826_0327'),
                ('mediamanager', '0004_auto_20160828_1825')]

    dependencies = [
        ('client_manager', '0001_initial'),
        ('mediamanager', '0002_auto_20160817_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='owner',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to='client_manager.Client'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='owner',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to='client_manager.Client'),
        ),
        migrations.AddField(
            model_name='tickerseries',
            name='owner',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to='client_manager.Client'),
        ),
    ]
