# Generated by Django 4.0.3 on 2022-04-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_accounts_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='approved',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
