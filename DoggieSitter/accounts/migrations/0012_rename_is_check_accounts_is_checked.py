# Generated by Django 4.0.3 on 2022-04-24 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_accounts_is_check'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='is_check',
            new_name='is_checked',
        ),
    ]