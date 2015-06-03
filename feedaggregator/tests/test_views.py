from django.test import TestCase
from feedaggregator.models import Item, Feed


class OPMLExportTests(TestCase):

    def setUp(self):
        Feed.objects.create(feed_url="http://example.com/feed.xml")

    def test_export_opml(self):
        """Export all the active feeds as OPML"""
        #test with active and inactive
        pass

class ParseFeedTests(TestCase):
    """
    Test errors when importing a Feed
    """
    pass


class FeedAggregatorTemplatetagsTest(TestCase):
    """
    Test the custom templatetags
    """
    pass
# http://stackoverflow.com/a/1690879/263989

class FeedViewsTest(TestCase):
    
    def setUp(self):
        # create feed and item

    def test_list(self):
        pass

    def test_detail(self):
        pass


class SyndicationTest(TestCase):

    def setUp(self):
        pass

    def test_rss(self):
        pass

    def test_atom(self):
        pass