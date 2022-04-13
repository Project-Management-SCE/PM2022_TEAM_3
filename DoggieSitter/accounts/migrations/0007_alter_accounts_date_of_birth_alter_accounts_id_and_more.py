# Generated by Django 4.0.3 on 2022-04-10 13:37

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_rename_age_accounts_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='id',
            field=models.CharField(max_length=9, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(9)]),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
