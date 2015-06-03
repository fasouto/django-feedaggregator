# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(default='<Unknown>', blank=True, verbose_name='name', max_length=255)),
                ('profile_url', models.URLField(blank=True, verbose_name='profile')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(default='<Untitled>', verbose_name='title', max_length=255)),
                ('feed_url', models.CharField(max_length=500, verbose_name='url', unique=True)),
                ('site_url', models.URLField(blank=True, verbose_name='site url')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('updated_on', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
                ('slug', models.SlugField(unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='added on')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='modified on')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(default='<Untitled>', verbose_name='title', max_length=255)),
                ('link', models.URLField(verbose_name='url', max_length=500)),
                ('guid', models.CharField(blank=True, max_length=500, null=True, verbose_name='global unique identifier')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('published_on', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
                ('slug', models.SlugField(unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='added on')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='modified on')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('authors', models.ManyToManyField(to='feedaggregator.Author', blank=True)),
                ('feed', models.ForeignKey(to='feedaggregator.Feed')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', to='taggit.Tag', through='taggit.TaggedItem', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-published_on'],
            },
        ),
    ]
