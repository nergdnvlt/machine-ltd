# Generated by Django 2.0.7 on 2018-07-24 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='distance',
            field=models.FloatField(null=True),
        ),
    ]
