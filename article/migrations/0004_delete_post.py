# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20180403_0833'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
