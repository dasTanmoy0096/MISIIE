# Generated by Django 5.0.6 on 2024-07-19 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MIS', '0009_rename_name_userbase_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cppp',
            old_name='tenderName',
            new_name='tenderTitle',
        ),
        migrations.RenameField(
            model_name='gem',
            old_name='gemName',
            new_name='gemTitle',
        ),
    ]
