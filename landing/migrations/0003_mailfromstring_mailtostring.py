# Generated by Django 2.2.2 on 2019-06-29 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20190629_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailFromString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_use_tls', models.BooleanField(default=True, verbose_name='EMAIL_USE_TLS(gmail.com, mail.ru)')),
                ('email_use_ssl', models.BooleanField(default=False, verbose_name='EMAIL_USE_SSL(yandex.ru)')),
                ('email_port', models.PositiveIntegerField(default=587, verbose_name='EMAIL_PORT')),
                ('email_host', models.CharField(default='smtp.gmail.com', max_length=250, verbose_name='EMAIL_HOST')),
                ('email_host_user', models.EmailField(default='goga23d@gmail.com', max_length=250, verbose_name='EMAIL_HOST_USER')),
                ('email_host_password', models.CharField(default='khysaqitvdnqtneg', max_length=250, verbose_name='EMAIL_HOST_PASSWORD')),
            ],
            options={
                'verbose_name': 'Откуда отправлять письмо',
                'verbose_name_plural': 'Откуда отправлять письмо',
            },
        ),
        migrations.CreateModel(
            name='MailToString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Кому отправлять письмо',
                'verbose_name_plural': 'Кому отправлять письмо',
            },
        ),
    ]