# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name='start date and time of the event')),
                ('end_date', models.DateTimeField(verbose_name='end date and time of the event')),
                ('image', models.FileField(upload_to='images/<built-in function id>')),
                ('description', models.CharField(max_length=800)),
                ('price', models.CharField(max_length=200)),
                ('reservation_required', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('other', models.CharField(max_length=200)),
            ],
        ),
    ]