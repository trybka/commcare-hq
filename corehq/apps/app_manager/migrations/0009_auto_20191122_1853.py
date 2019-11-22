# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-11-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_manager', '0008_remove_uses_master_app_form_ids'),
    ]

    operations = [
        migrations.CreateModel(
            name='SQLGlobalAppConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=255)),
                ('app_id', models.CharField(max_length=255)),
                ('app_prompt', models.CharField(choices=[('on', 'on'), ('off', 'off'), ('forced', 'forced')], default='off', max_length=32)),
                ('apk_prompt', models.CharField(choices=[('on', 'on'), ('off', 'off'), ('forced', 'forced')], default='off', max_length=32)),
                ('apk_version', models.CharField(max_length=32)),
                ('app_version', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='sqlglobalappconfig',
            unique_together=set([('domain', 'app_id')]),
        ),
    ]
