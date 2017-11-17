# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 09:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_client', models.CharField(choices=[('Ф', 'Фізична особа'), ('Ю', 'Юридична особа')], default='Ф', max_length=1, verbose_name='Тип клієнта')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name="Ім'я")),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Прізвище')),
                ('sur_name', models.CharField(blank=True, max_length=50, verbose_name='По батькові')),
                ('full_name', models.CharField(blank=True, max_length=200, verbose_name='Повна назва')),
                ('phone_mobile', models.CharField(max_length=15, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Електронна адреса')),
                ('url_site', models.URLField(blank=True, verbose_name='Сайт')),
                ('address', models.CharField(max_length=300, verbose_name='Адреса')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]