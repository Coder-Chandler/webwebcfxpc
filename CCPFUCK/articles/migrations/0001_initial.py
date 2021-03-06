# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-01 16:29
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u6587\u7ae0\u540d')),
                ('desc', models.CharField(max_length=300, verbose_name='\u6587\u7ae0\u63cf\u8ff0')),
                ('article_belong', models.CharField(max_length=50, verbose_name='\u7c7b\u522b')),
                ('detail', DjangoUeditor.models.UEditorField(default='', verbose_name='\u6587\u7ae0\u5185\u5bb9')),
                ('image', models.ImageField(upload_to='article/%Y/%m', verbose_name='\u5c01\u9762\u56fe')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('is_banner', models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6e\u64ad')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u89c6\u9891\u540d')),
                ('times', models.IntegerField(default=0, verbose_name='\u65f6\u957f(\u5206\u949f)')),
                ('url', models.CharField(default='', max_length=200, verbose_name='\u8bbf\u95ee\u5730\u5740')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Articles', verbose_name='\u6587\u7ae0')),
            ],
            options={
                'verbose_name': '\u89c6\u9891',
                'verbose_name_plural': '\u89c6\u9891',
            },
        ),
        migrations.CreateModel(
            name='BannerArticle',
            fields=[
            ],
            options={
                'verbose_name': '\u8f6e\u64ad\u6587\u7ae0',
                'proxy': True,
                'verbose_name_plural': '\u8f6e\u64ad\u6587\u7ae0',
            },
            bases=('articles.articles',),
        ),
    ]
