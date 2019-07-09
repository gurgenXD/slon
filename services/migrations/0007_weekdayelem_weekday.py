# Generated by Django 2.2.2 on 2019-07-09 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_weekdayelem'),
    ]

    operations = [
        migrations.AddField(
            model_name='weekdayelem',
            name='weekday',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='weekday_elems', to='services.WeekDay', verbose_name='День недели'),
            preserve_default=False,
        ),
    ]