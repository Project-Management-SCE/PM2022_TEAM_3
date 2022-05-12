# Generated by Django 4.0.3 on 2022-04-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_accounts_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='address',
            field=models.CharField(default='Empty', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accounts',
            name='is_doggiesitter',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
