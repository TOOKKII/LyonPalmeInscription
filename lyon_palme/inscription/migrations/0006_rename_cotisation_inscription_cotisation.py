# Generated by Django 4.1.3 on 2023-06-09 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0005_inscription_cotisation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscription',
            old_name='Cotisation',
            new_name='cotisation',
        ),
    ]
