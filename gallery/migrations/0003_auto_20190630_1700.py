# Generated by Django 2.2.2 on 2019-06-30 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20190630_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=250, unique=True, verbose_name='Название'),
        ),
    ]
