# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-21 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1, null=True)),
                ('name', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]