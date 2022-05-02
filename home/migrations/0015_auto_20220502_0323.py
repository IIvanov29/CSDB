# Generated by Django 3.2.12 on 2022-05-02 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_tutorial_tutorial_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_category',
            field=models.CharField(choices=[('cstools', 'Cyber Sec Tools'), ('networking', 'Networking'), ('csbasics', 'Cyber Security Basics'), ('programming', 'Programming')], max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_link',
            field=models.URLField(blank=True),
        ),
    ]
