# Generated by Django 4.1.3 on 2022-11-28 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_vacancy_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['id', 'text', 'slug', 'status', 'created', 'user'], 'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
    ]
