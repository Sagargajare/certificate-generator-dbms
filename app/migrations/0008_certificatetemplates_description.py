# Generated by Django 3.2.9 on 2021-11-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_certificatetemplates'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificatetemplates',
            name='description',
            field=models.TextField(default='', max_length=500),
            preserve_default=False,
        ),
    ]