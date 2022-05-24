# Generated by Django 4.0.3 on 2022-05-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_alter_postfeedback_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='Aprt',
            new_name='aprt',
        ),
        migrations.AlterField(
            model_name='trip',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='trip',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='dog_owner',
            field=models.CharField(max_length=50),
        ),
    ]