# Generated by Django 4.1.4 on 2022-12-15 02:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('random_app', '0007_remove_csv_data_activated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv_data',
            name='file_name',
            field=models.FileField(upload_to='random_app', validators=[django.core.validators.FileExtensionValidator(['csv'])]),
        ),
    ]
