# Generated by Django 3.2.12 on 2022-04-23 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_submission_is_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='date_sumbmitted',
            new_name='date_submitted',
        ),
    ]
