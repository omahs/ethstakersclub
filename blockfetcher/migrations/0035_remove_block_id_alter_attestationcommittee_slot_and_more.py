# Generated by Django 4.2.1 on 2023-05-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockfetcher', '0034_remove_attestationcommittee_blockfetche_validat_70f015_gin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='id',
        ),
        migrations.AlterField(
            model_name='attestationcommittee',
            name='slot',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='block',
            name='slot_number',
            field=models.PositiveIntegerField(db_index=True, primary_key=True, serialize=False, unique=True),
        ),
    ]