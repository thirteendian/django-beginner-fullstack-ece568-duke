# Generated by Django 3.2.11 on 2022-01-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20220128_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='special_request',
            field=models.CharField(blank=True, default=' ', max_length=20),
        ),
    ]