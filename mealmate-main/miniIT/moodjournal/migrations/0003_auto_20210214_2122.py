# Generated by Django 3.1.5 on 2021-02-14 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moodjournal', '0002_auto_20210214_2104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='en_choice',
            new_name='energy',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='hp_choice',
            new_name='happiness',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='he_choice',
            new_name='health',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='hu_choice',
            new_name='hunger',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='st_choice',
            new_name='stress',
        ),
    ]
