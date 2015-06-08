from django.contrib.syndication.views import Feed as DjangoFeed
from django.core.urlresolvers import reverse
from django.utils.feedgenerator import Atom1Feed

from feedaggregator.models import Item, Feed
from feedaggregator.settings import FEEDAGGREGATOR_TITLE, FEEDAGGREGATOR_RSS_SIZE, FEEDAGGREGATOR_RSS_DESCRIPTION


class LatestItemsFeed(DjangoFeed):
    title = FEEDAGGREGATOR_TITLE
    description = FEEDAGGREGATOR_RSS_DESCRIPTION

    def items(self):
        return Item.active.order_by('-date_modified')[:FEEDAGGREGATOR_RSS_SIZE]

    def link(self):
        return reverse("feedaggregator:rss_latest_items")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_published(self, item):
        return item.published_on


class AtomLatestItemsFeed(LatestItemsFeed):
    feed_type = Atom1Feed
    subtitle = LatestItemsFeed.description
