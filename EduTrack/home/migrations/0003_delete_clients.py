# Generated by Django 4.2.6 on 2023-11-25 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_clients'),
    ]

    operations = [
        migrations.DeleteModel(
            name='clients',
        ),
    ]