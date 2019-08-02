# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-05 17:16
from __future__ import absolute_import, unicode_literals

from django.db import migrations

from corehq.sql_db.operations import RawSQLMigration

migrator = RawSQLMigration(('custom', 'icds_reports', 'migrations', 'sql_templates'))


class Migration(migrations.Migration):

    dependencies = [
        ('icds_reports', '0037_add_new_infra_data'),
    ]

    operations = [
        migrator.get_migration('update_tables19.sql'),
    ]
