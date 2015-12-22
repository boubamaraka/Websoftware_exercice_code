# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('text_body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogSite',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('pretty_url', models.CharField(max_length=20, unique=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='blog',
            field=models.ForeignKey(to='blog.BlogSite'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='in_reply_to',
            field=models.ForeignKey(null=True, to='blog.BlogPost', blank=True),
        ),
    ]
