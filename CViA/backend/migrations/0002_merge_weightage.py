# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weightage',
            name='job_description',
        ),
        migrations.AddField(
            model_name='jobdescription',
            name='education_weightage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='jobdescription',
            name='experience_weightage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='jobdescription',
            name='languages_weightage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='jobdescription',
            name='skills_weightage',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='Weightage',
        ),
    ]
