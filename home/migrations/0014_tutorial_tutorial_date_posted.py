# Generated by Django 3.2.12 on 2022-04-25 04:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_tutorial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_date_posted',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
