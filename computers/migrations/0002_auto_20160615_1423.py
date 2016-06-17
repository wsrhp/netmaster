# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='user',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
