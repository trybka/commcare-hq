# Generated by Django 1.11.14 on 2018-08-07 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_processor', '0075_auto_20181026_0951'),
    ]

    operations = [
        migrations.RenameModel("XFormAttachmentSQL", "DeprecatedXFormAttachmentSQL"),
        migrations.SeparateDatabaseAndState(
            database_operations=[
                # drop foreign key constraint
                migrations.AlterField(
                    model_name='DeprecatedXFormAttachmentSQL',
                    name='form',
                    field=models.ForeignKey(
                        'XFormInstanceSQL',
                        to_field='form_id',
                        db_index=False,
                        db_constraint=False,
                        on_delete=models.CASCADE,
                    )
                ),
            ],
            state_operations=[
                # update model state (Django only, does not affect database)
                migrations.RenameField(
                    model_name='DeprecatedXFormAttachmentSQL',
                    old_name='form',
                    new_name='form_id'
                ),
                migrations.AlterField(
                    model_name='DeprecatedXFormAttachmentSQL',
                    name='form_id',
                    field=models.CharField(max_length=255)
                ),
                migrations.AlterField(
                    model_name='caseattachmentsql',
                    name='blob_bucket',
                    field=models.CharField(default='', max_length=255, null=True),
                ),
                migrations.AlterField(
                    model_name='caseattachmentsql',
                    name='md5',
                    field=models.CharField(default='', max_length=255),
                ),
            ],
        ),
    ]
