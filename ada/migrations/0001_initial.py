# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('model_pic', models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'images')),
                ('theme', models.CharField(default=b'none', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_text', models.CharField(max_length=200)),
                ('breed_text', models.CharField(max_length=100)),
                ('color_text', models.CharField(max_length=100)),
                ('age_text', models.CharField(max_length=100)),
                ('size_text', models.CharField(max_length=100)),
                ('sex_text', models.CharField(max_length=100)),
                ('info_text', models.CharField(max_length=500)),
                ('story_text', models.CharField(max_length=1000)),
                ('model_pic', models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'images')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published')),
            ],
        ),
    ]
