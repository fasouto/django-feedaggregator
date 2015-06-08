# -*- coding: utf-8 -*-
from celery import task
from time import mktime
from datetime import datetime
import logging

import feedparser

from feedaggregator.settings import FEEDAGGREGATOR_TAGS_LOWERCASE
from feedaggregator.models import Item

logger = logging.getLogger(__name__)


@task
def update_feed(feed):
    """
    Update the feed content and fetch latest items.
    """
    logger.debug("Processing feed %s" % feed)
    parsed_feed = feedparser.parse(feed.feed_url)

    if parsed_feed.bozo:  # Handle error in feed
        logger.error("Error in feed %s: %s" % (feed.feed_url, parsed_feed.bozo_exception))
        return

    if feed.is_new:
        title = parsed_feed.feed.get('title', "-")
        if not title:  # Check for empty strings
            title = "<Untitled>"

        link = parsed_feed.feed.get('link')
        description = parsed_feed.feed.get('description', "")

        if 'updated_parsed' in parsed_feed.feed:
            feed.updated_on = datetime.fromtimestamp(mktime(parsed_feed.feed.updated_parsed))

        # Save the feed info in the db
        feed.title = title
        feed.site_url = link
        feed.description = description
        feed.save()

    # Save the feed items
    for entry in parsed_feed.entries:
        if all(k in entry for k in ("title", "link")):
            print(entry)
            entry_title = entry.get('title', "<Untitled>")
            if not entry_title:  # Check for empty strings
                entry_title = "<Untitled>"

            # Sometimes feed titles change, this is why we don't user get_or_create
            try:
                feed_item = Item.objects.get(feed=feed, link=entry.link)
                feed_item.title = entry_title[:255]
            except Item.DoesNotExist:
                feed_item = Item(feed=feed, link=entry.link, title=entry_title[:255])

            feed_item.description = entry.get('description', "")
            feed_item.guid = entry.get('id', "")

            if 'published_parsed' in entry:
                feed_item.published_on = datetime.fromtimestamp(mktime(entry.published_parsed))
            feed_item.save()

            # Add the tags
            for tag_dict in entry.get('tags', ''):
                term = tag_dict.get('term', '')
                if FEEDAGGREGATOR_TAGS_LOWERCASE:
                    term = term.lower()
                feed_item.tags.add(term)
