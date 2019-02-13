# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 19:08
from __future__ import absolute_import
from __future__ import unicode_literals

import datetime

import partial_index
from django.db import migrations, models

import corehq.blobs.models
import corehq.blobs.util
from corehq.sql_db.migrations import partitioned
from corehq.sql_db.operations import RawSQLMigration


migrator = RawSQLMigration(('corehq', 'blobs', 'sql_templates'), {})


@partitioned
class Migration(migrations.Migration):

    dependencies = [
        ('blobs', '0001_squashed_0009_domains'),
        ('form_processor', '0072_case_attachment_drops'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlobMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=255)),
                ('parent_id', models.CharField(help_text='Parent primary key or unique identifier', max_length=255)),  # noqa: E501
                ('name', models.CharField(default='', help_text='Optional blob name.\n\n        This field is intended to be used by doc types having multiple\n        blobs associated with a single document.\n        ', max_length=255),),  # noqa: E501
                ('key', models.CharField(default=corehq.blobs.models.uuid4_hex, help_text="Blob key in the external blob store.\n\n        This must be a globally unique value. Historically this was\n        `blob_bucket + '/' + identifier` for blobs associated with a\n        couch document. Could be a UUID or the result of\n        `util.random_url_id(16)`. Defaults to `uuid4().hex`.\n        ", max_length=255)),  # noqa: E501
                ('type_code', models.PositiveSmallIntegerField(help_text='Blob type code. See `corehq.blobs.CODES`.')),  # noqa: E501
                ('content_length', models.PositiveIntegerField()),
                ('content_type', models.CharField(max_length=255, null=True)),
                ('properties', corehq.blobs.util.NullJsonField(default=dict)),
                ('created_on', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('expires_on', models.DateTimeField(default=None, null=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='blobmeta',
            index=partial_index.PartialIndex(fields=['expires_on'], name='blobs_blobm_expires_64b92d_partial', unique=False, where='expires_on IS NOT NULL', where_postgresql=b'', where_sqlite=b''),  # noqa: E501
        ),
        migrations.AlterIndexTogether(
            name='blobmeta',
            index_together=set([('parent_id', 'type_code', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='blobmeta',
            unique_together=set([('key',)]),
        ),
        partitioned(migrator.get_migration('delete_blob_meta.sql'), apply_to_proxy=False),
    ]
