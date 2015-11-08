# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_change_job_description_experience_to_float'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdescription',
            name='education_weightage',
            field=models.FloatField(default=1L),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='experience_weightage',
            field=models.FloatField(default=1L),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='languages_weightage',
            field=models.FloatField(default=1L),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='skills_weightage',
            field=models.FloatField(default=1L),
        ),
    ]
