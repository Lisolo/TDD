# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20140809_0221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': (b'id',)},
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default=b'', unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([(b'list', b'text')]),
        ),
    ]
