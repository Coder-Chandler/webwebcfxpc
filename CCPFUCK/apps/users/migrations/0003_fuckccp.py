# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-02 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fuckccp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_ccp_num', models.CharField(blank=True, max_length=11, null=True)),
            ],
            options={
                'verbose_name': '\u9000\u515a\u4eba\u6570',
                'verbose_name_plural': '\u9000\u515a\u4eba\u6570',
            },
        ),
    ]
