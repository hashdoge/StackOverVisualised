# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-11 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_janjson'),
    ]

    operations = [
        migrations.CreateModel(
            name='JanCsv',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tags', models.CharField(max_length=10000)),
                ('score', models.IntegerField(max_length=20)),
            ],
        ),
    ]