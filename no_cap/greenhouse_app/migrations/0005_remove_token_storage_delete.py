# Generated by Django 4.1.4 on 2023-01-11 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greenhouse_app', '0004_token_storage_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token_storage',
            name='delete',
        ),
    ]
