# Generated by Django 4.0.3 on 2022-04-10 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_accounts_age_accounts_approved_accounts_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='age',
            new_name='date_of_birth',
        ),
    ]