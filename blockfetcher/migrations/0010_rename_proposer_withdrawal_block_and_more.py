# Generated by Django 4.1.9 on 2023-05-21 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blockfetcher', '0009_withdrawal_proposer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='withdrawal',
            old_name='proposer',
            new_name='block',
        ),
        migrations.RemoveField(
            model_name='withdrawal',
            name='epoch_number',
        ),
    ]