# Generated by Django 2.2.2 on 2019-06-29 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='social',
            old_name='social',
            new_name='link',
        ),
    ]
