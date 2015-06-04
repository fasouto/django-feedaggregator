# -*- coding: utf-8 -*-

from django.db import models


class FeedManager(models.Manager):
    def new_feeds(self):
        """
        Get the feeds that have never been fetched
        """
        return super(FeedManager, self).get_query_set().filter(is_new=True)

    def get_queryset(self):
        return super(FeedManager, self).get_queryset().filter(is_active=True)


class ItemManager(models.Manager):
    def get_queryset(self):
        return super(ItemManager, self).get_queryset().filter(is_active=True)
