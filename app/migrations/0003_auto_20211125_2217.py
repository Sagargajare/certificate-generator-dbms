# Generated by Django 3.2.9 on 2021-11-25 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_certificate_uniqueid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='date',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='expiry',
        ),
    ]