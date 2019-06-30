# Generated by Django 2.2.2 on 2019-06-30 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booknow', '0002_note_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='sex',
            field=models.CharField(choices=[('boy', 'Мальчик'), ('girl', 'Девочка')], default='boy', max_length=20, verbose_name='Пол ребенка'),
        ),
    ]
