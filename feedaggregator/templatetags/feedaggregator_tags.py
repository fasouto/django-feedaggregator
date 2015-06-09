# -*- coding: utf-8 -*-

from django import template

from feedaggregator.models import Feed, Item

register = template.Library()


@register.inclusion_tag('feedaggregator/tags/feed_list.html')
def feedaggregator_feed_list(limit=None):
    """
    Show all the active feeds
    """
    feeds = Feed.active.all()[:limit]
    return {'feeds': feeds}


@register.inclusion_tag('feedaggregator/tags/item_list.html')
def feedaggregator_latest_items(limit=10):
    """
    Show the latest items
    """
    items = Item.active.all()[:limit]
    return {'items': items}


@register.inclusion_tag('feedaggregator/tags/tag_list.html')
def feedaggregator_popular_tags(limit=10):
    """
    Show the most used tags
    """
    tags = Item.tags.most_common()[:limit]
    return {'tags': tags}
