# -*- coding: utf-8 -*-
from django.test import TestCase, override_settings
from django.core.urlresolvers import reverse
from django.conf import settings

from feedaggregator.models import Item, Feed


class OPMLExportTests(TestCase):

    def setUp(self):
        self.opml_example = b'<?xml version="1.0" encoding="UTF-8"?>\n<opml version="1.1">\n  <head>\n    <title>example.com</title>\n  </head>\n  <body>\n    \n      <outline text="Some feed" title="Some feed" htmlUrl="" xmlUrl="http://example.com/feed.xml" type="rss" />\n    \n  </body>\n</opml>\n'
        Feed.objects.create(feed_url="http://example.com/feed.xml", title="Some feed")

    def test_export_opml(self):
        """Export all the active feeds as OPML"""
        response = self.client.get(reverse('feedaggregator:opml'))
        self.assertEqual(response.content, self.opml_example)
    

class FeedViewsTest(TestCase):
    
    def setUp(self):
        self.test_feed = Feed.objects.create(feed_url="http://example.com/feed.xml")
        self.test_item = Item.objects.create(feed=self.test_feed, link="http://example.com/feedaggregator-news", title="Some title")

    def test_index(self):
        response = self.client.get(reverse('feedaggregator:item_list'))
        self.assertEqual(response.status_code, 200) 
        self.assertTrue('item_list' in response.context)

    def test_item_detail(self):
        response = self.client.get(reverse('feedaggregator:item_detail', kwargs={'slug': self.test_item.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('item' in response.context)

        response = self.client.get(reverse('feedaggregator:item_detail', kwargs={'slug': "Foo"}))
        self.assertEqual(response.status_code, 404)

    def test_feed_detail(self):
        response = self.client.get(reverse('feedaggregator:feed_detail', kwargs={'slug': self.test_feed.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('item_list' in response.context)

        response = self.client.get(reverse('feedaggregator:item_detail', kwargs={'slug': "Foo"}))
        self.assertEqual(response.status_code, 404)

class SyndicationTest(TestCase):

    def setUp(self):
        self.rss_example = b'<?xml version="1.0" encoding="utf-8"?>\n<rss xmlns:atom="http://www.w3.org/2005/Atom" version="2.0"><channel><title>Latest posts</title><link>http://example.com/feed/rss/</link><description></description><atom:link href="http://example.com/feed/rss/" rel="self"></atom:link><language>en-us</language><lastBuildDate>Thu, 04 Jun 2015 14:23:06 -0000</lastBuildDate></channel></rss>'
        self.test_feed = Feed.objects.create(feed_url="http://example.com/feed.xml", title="Some feed")

    def test_rss(self):
        response = self.client.get(reverse('feedaggregator:rss_latest_items'))
        self.assertEqual(response.status_code, 200) 

    def test_atom(self):
        response = self.client.get(reverse('feedaggregator:atom_latest_items'))
        self.assertEqual(response.status_code, 200) 