# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-03-30 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.FileField(default='avatar/default.jpg', upload_to='avatar/', verbose_name='创建时间'),
        ),
    ]
