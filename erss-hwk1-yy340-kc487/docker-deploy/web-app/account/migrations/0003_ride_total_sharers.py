# Generated by Django 3.2.11 on 2022-01-28 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_driver_myuser_ride'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='total_sharers',
            field=models.IntegerField(null=True),
        ),
    ]
