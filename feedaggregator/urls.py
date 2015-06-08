# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from feedaggregator.views import ItemList, ItemDetail, FeedDetail, FeedList, TagDetail, TagList, TagCloud
from feedaggregator.feeds import LatestItemsFeed, AtomLatestItemsFeed


urlpatterns = patterns('feedaggregator.views',
    # Items
    url(r'^$', ItemList.as_view(), name="item_list"),
    url(r'^item/(?P<slug>[-\w]+)/$', ItemDetail.as_view(), name="item_detail"),

    # Feeds
    url(r'^feeds/$', FeedList.as_view(), name="feed_list"),
    url(r'^feeds/(?P<slug>[-\w]+)/$', FeedDetail.as_view(), name="feed_detail"),

    # Tags
    url(r'^tags/$', TagList.as_view(), name="tag_list"),
    url(r'^tag/(?P<tag>[-\w]+)/$', TagDetail.as_view(), name="tag_detail"),

    # Tag cloud
    url(r'^cloud/$', TagCloud.as_view(), name="tag_cloud"),

    # OPML
    url(r'^opml.xml$', 'export_opml', name="opml"),
)

# Feed's urls
urlpatterns += patterns('',
    url(r'^feed/rss/$', LatestItemsFeed(), name="rss_latest_items"),
    url(r'^feed/atom/$', AtomLatestItemsFeed(), name="atom_latest_items")
)
