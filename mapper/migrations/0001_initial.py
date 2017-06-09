# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-08 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('complaint', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapperNGO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_name', models.CharField(blank=True, max_length=50)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='complaint.Category')),
            ],
        ),
    ]