# Generated by Django 4.0.3 on 2022-04-24 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_accounts_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='is_check',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]