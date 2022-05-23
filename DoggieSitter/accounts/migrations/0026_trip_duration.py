# Generated by Django 4.0.3 on 2022-05-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_trip_endtime_trip_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='duration',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]
