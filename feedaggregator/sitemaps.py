from django.contrib.sitemaps import Sitemap
from feedaggregator.models import Feed, Item


class ItemSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Item.active.all()

    def lastmod(self, obj):
        return obj.published_on


class FeedSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Feed.active.all()

    def lastmod(self, obj):
        return obj.updated_on
