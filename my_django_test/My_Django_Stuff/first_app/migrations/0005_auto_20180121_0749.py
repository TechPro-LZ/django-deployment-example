# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-21 07:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_userinfo_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='company',
            new_name='email',
        ),
    ]
