# Generated by Django 4.1.3 on 2022-11-28 01:53

from django.db import migrations, models
import vacancies.models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_vacancy_min_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='updated_at',
            field=models.DateField(null=True, validators=[vacancies.models.chec_date_not_past]),
        ),
    ]