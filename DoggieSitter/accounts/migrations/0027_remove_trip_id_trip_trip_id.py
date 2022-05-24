# Generated by Django 4.0.3 on 2022-05-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_trip_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='id',
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]