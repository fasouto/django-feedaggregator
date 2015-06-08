# -*- coding: utf-8 -*-
"""
Go trough all the feeds and updates them
"""

import logging
from optparse import make_option

from django.core.management.base import BaseCommand
from django.contrib.sitemaps import ping_google

from feedaggregator.tasks import update_feed
from feedaggregator.models import Feed, Item

logger = logging.getLogger('feedaggregator')


class Command(BaseCommand):
    args = None
    help = "Update all the feeds"

    option_list = BaseCommand.option_list + (
        make_option('--verbose',
                    action='store_true',
                    dest='verbose',
                    default=False,
                    help='Output progress'),
    )

    def handle(self, *args, **options):
        for feed in Feed.objects.all():
            update_feed(feed)
        ping_google()  # tell google to reindex the site
        logger.info("Feeds updated")
