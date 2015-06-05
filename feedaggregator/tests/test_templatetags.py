# -*- coding: utf-8 -*-
from django.test import TestCase, override_settings
from django.template import Template, Context
from django.core.urlresolvers import reverse
from django.conf import settings

from feedaggregator.models import Item, Feed


class FeedAggregatorFeedListTag(TestCase):
    """
    Test the custom feedaggregator_feed_list template tag
    """

    TEMPLATE = Template("{% load feedaggregator_tags %} {% feedaggregator_feed_list %}")
    LIMITED_TEMPLATE = Template("{% load feedaggregator_tags %} {% feedaggregator_feed_list 1 %}")

    def setUp(self):
        self.test_feed = Feed.objects.create(feed_url="http://example.com/feed.xml", title="Foo")
        self.another_test_feed = Feed.objects.create(feed_url="http://example.com/feed2.xml", title="Bar")
 
    def test_feed_shows_up(self):
        rendered = self.TEMPLATE.render(Context({}))
        self.assertIn(self.another_test_feed.title, rendered)

    def test_limit_results(self):
        rendered = self.LIMITED_TEMPLATE.render(Context({}))
        self.assertIn(self.another_test_feed.title, rendered)
        self.assertNotIn(self.test_feed.title, rendered)


class FeedAggregatorLatestItems(TestCase):
    """
    Test the custom feedaggregator_latest_items template tag
    """

    TEMPLATE = Template("{% load feedaggregator_tags %} {% feedaggregator_latest_items %}")
    LIMITED_TEMPLATE = Template("{% load feedaggregator_tags %} {% feedaggregator_latest_items 1 %}")

    def setUp(self):
        self.test_feed = Feed.objects.create(feed_url="http://example.com/feed.xml", title="Foo")
        self.inactive_item = Item.objects.create(feed=self.test_feed, link="http://example.com/feedaggregator-inactive", title="Inactive item", is_active=False)
        self.first_item = Item.objects.create(feed=self.test_feed, link="http://example.com/feedaggregator1", title="First title")
        self.second_item = Item.objects.create(feed=self.test_feed, link="http://example.com/feedaggregator2", title="Second title")

    def test_items_shows_up(self):
        rendered = self.TEMPLATE.render(Context({}))
        self.assertIn(self.first_item.title, rendered)

    def test_limit_results(self):
        rendered = self.LIMITED_TEMPLATE.render(Context({}))
        self.assertIn(self.first_item.title, rendered)
        self.assertNotIn(self.second_item.title, rendered)


class FeedAggregatorPopularTags(TestCase):
    """
    Test the custom feedaggregator_latest_items template tag
    """

    TEMPLATE = Template("{% load feedaggregator_tags %} {% feedaggregator_popular_tags %}")
    LIMITED_TEMPLATE = Template("{% load feedaggregator_tags %} {% feedaggregator_popular_tags 1 %}")

    def setUp(self):
        self.test_feed = Feed.objects.create(feed_url="http://example.com/feed.xml", title="Foo")
        self.first_item = Item.objects.create(feed=self.test_feed, link="http://example.com/feedaggregator1", title="First title")
        self.second_item = Item.objects.create(feed=self.test_feed, link="http://example.com/feedaggregator2", title="Second title")
        self.first_item.tags.add('python', 'django', 'bar')
        self.second_item.tags.add('python', 'foo')

    def test_items_shows_up(self):
        rendered = self.TEMPLATE.render(Context({}))
        self.assertIn('python', rendered)
        self.assertNotIn('flask', rendered)

    def test_limit_results(self):
        rendered = self.LIMITED_TEMPLATE.render(Context({}))
        self.assertIn('python', rendered)
        self.assertNotIn('django', rendered)
