# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_merge_weightage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdescription',
            name='experience',
            field=models.FloatField(),
        ),
    ]
