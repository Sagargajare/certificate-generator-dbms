# Generated by Django 3.2.9 on 2021-11-25 16:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211125_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='expiry',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
