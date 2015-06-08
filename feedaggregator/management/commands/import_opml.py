# -*- coding: utf-8 -*-
"""
Import an OPML file into the database
http://en.wikipedia.org/wiki/OPML
"""
import listparser
import logging
from optparse import make_option
from django.core.management.base import BaseCommand

from feedaggregator.models import Feed, Item

logger = logging.getLogger('feedaggregator')


class Command(BaseCommand):
    args = None
    help = "Import feeds from an OPML file"

    def add_arguments(self, parser):
        parser.add_argument('opml_file', nargs='+')

    def fill_feed_info(self, opml_file):
        """
        Import the file
        """
        parsed = listparser.parse(opml_file)
        for feed in parsed.feeds:
            print("Adding %s" % feed.url)
            Feed.objects.get_or_create(feed_url=feed.url)

    def handle(self, *args, **options):
        opml_file = options['opml_file'][0]
        self.fill_feed_info(opml_file)
        logger.info("OPML file imported successfully")
