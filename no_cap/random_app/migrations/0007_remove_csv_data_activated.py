# Generated by Django 4.1.3 on 2022-12-10 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('random_app', '0006_csv_data_activated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csv_data',
            name='activated',
        ),
    ]
