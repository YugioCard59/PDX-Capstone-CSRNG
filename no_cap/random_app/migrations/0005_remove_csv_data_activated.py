# Generated by Django 4.1.3 on 2022-12-10 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('random_app', '0004_delete_table_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csv_data',
            name='activated',
        ),
    ]
