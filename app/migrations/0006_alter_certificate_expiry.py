# Generated by Django 3.2.9 on 2021-11-25 16:52

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211125_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='expiry',
            field=models.DateTimeField(default=app.models.return_date_time),
        ),
    ]