# Generated by Django 4.1.3 on 2022-11-27 14:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='min_experience',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
