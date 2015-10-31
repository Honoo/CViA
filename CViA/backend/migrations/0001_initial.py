# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_title', models.TextField()),
                ('description', models.TextField()),
                ('skills', models.TextField()),
                ('experience', models.TextField()),
                ('education', models.TextField()),
                ('languages', models.TextField()),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('skills', models.TextField()),
                ('experience', models.TextField()),
                ('education', models.TextField()),
                ('awards', models.TextField()),
                ('honors', models.TextField()),
                ('languages', models.TextField()),
                ('personal_references', models.TextField()),
                ('interests', models.TextField()),
                ('technology', models.TextField()),
                ('certification', models.TextField()),
                ('projects', models.TextField()),
                ('summary', models.TextField()),
                ('objective', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Weightage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skills_weightage', models.FloatField()),
                ('education_weightage', models.FloatField()),
                ('languages_weightage', models.FloatField()),
                ('experience_weightage', models.FloatField()),
                ('job_description', models.ForeignKey(to='backend.JobDescription')),
            ],
        ),
    ]
