# Generated by Django 2.1.3 on 2018-11-27 10:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20181127_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='privacy_acceptance_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='terms_acceptance_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
