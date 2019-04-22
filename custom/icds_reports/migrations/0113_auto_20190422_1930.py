# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-22 19:30
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icds_reports', '0112_citusdashboarddiff_citusdashboardexception_citusdashboardtiming'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citusdashboarddiff',
            name='args',
        ),
        migrations.RemoveField(
            model_name='citusdashboarddiff',
            name='function_name',
        ),
        migrations.RemoveField(
            model_name='citusdashboarddiff',
            name='kwargs',
        ),
        migrations.RemoveField(
            model_name='citusdashboardexception',
            name='args',
        ),
        migrations.RemoveField(
            model_name='citusdashboardexception',
            name='function_name',
        ),
        migrations.RemoveField(
            model_name='citusdashboardexception',
            name='kwargs',
        ),
        migrations.RemoveField(
            model_name='citusdashboardtiming',
            name='args',
        ),
        migrations.RemoveField(
            model_name='citusdashboardtiming',
            name='function_name',
        ),
        migrations.RemoveField(
            model_name='citusdashboardtiming',
            name='kwargs',
        ),
        migrations.AddField(
            model_name='citusdashboarddiff',
            name='context',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='citusdashboarddiff',
            name='data_source',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='citusdashboardexception',
            name='context',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='citusdashboardexception',
            name='data_source',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='citusdashboardtiming',
            name='context',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='citusdashboardtiming',
            name='data_source',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
