# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0004_product_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(verbose_name=b'url', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='', unique=True, max_length=255),
            preserve_default=False,
        ),
    ]
