# Generated by Django 4.1.3 on 2022-11-26 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('hr', 'hr'), ('seeker', 'seeker'), ('unknown', 'unknown')], default='unknown', max_length=7),
        ),
    ]
