# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0002_auto_20160615_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='name',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
