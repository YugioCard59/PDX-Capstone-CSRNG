# Generated by Django 4.1.4 on 2023-01-04 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greenhouse_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token_storage',
            name='token_user',
        ),
    ]