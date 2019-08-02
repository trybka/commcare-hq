# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-06 18:29
from __future__ import absolute_import, unicode_literals

from django.db import migrations

from corehq.sql_db.operations import RawSQLMigration

migrator = RawSQLMigration(('custom', 'icds_reports', 'migrations', 'sql_templates'))


class Migration(migrations.Migration):

    dependencies = [
        ('icds_reports', '0039_add_agg_thr_forms_table'),
    ]

    operations = [
        migrator.get_migration('update_tables20.sql'),
    ]
