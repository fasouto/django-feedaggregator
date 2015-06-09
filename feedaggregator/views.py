# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.sites.shortcuts import get_current_site

from taggit.models import Tag

from feedaggregator.models import Feed, Item
from feedaggregator.settings import FEEDAGGREGATOR_PAGE_SIZE


class FeedList(ListView):
    """
    List all the active feeds
    """
    model = Feed
    context_object_name = "feed_list"
    paginate_by = FEEDAGGREGATOR_PAGE_SIZE

    def get_queryset(self):
        return Feed.active.all()


class FeedDetail(ListView):
    """
    Show an feed information.
    Used a listview instead of a detailview to use pagination easily
    """
    model = Item
    context_object_name = "item_list"
    template_name = "feedaggregator/feed_detail.html"
    paginate_by = FEEDAGGREGATOR_PAGE_SIZE

    def get_context_data(self, **kwargs):
        context = super(FeedDetail, self).get_context_data(**kwargs)
        context['feed'] = Feed.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return Item.active.filter(feed__slug=self.kwargs['slug'])


class ItemList(ListView):
    """
    List of all the active items
    """
    model = Item
    context_object_name = "item_list"
    paginate_by = FEEDAGGREGATOR_PAGE_SIZE

    def get_queryset(self):
        return Item.active.all()


class ItemDetail(DetailView):
    """
    Show an individual item
    """
    model = Item
    context_object_name = "item"


class TagList(ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "feedaggregator/tag_list.html"
    paginate_by = FEEDAGGREGATOR_PAGE_SIZE


class TagDetail(ListView):
    """
    Show all the items that have that tag
    """
    model = Item
    context_object_name = "item_list"
    template_name = "feedaggregator/tag_detail.html"
    paginate_by = FEEDAGGREGATOR_PAGE_SIZE

    def get_context_data(self, **kwargs):
        context = super(TagDetail, self).get_context_data(**kwargs)
        context['tag'] = Tag.objects.get(slug=self.kwargs['tag'])
        return context

    def get_queryset(self):
        return Item.active.filter(tags__slug__in=[self.kwargs['tag']])


class TagCloud(TemplateView):
    template_name = "feedaggregator/tag_cloud.html"


def export_opml(request):
    """
    Generate an OPML file with the active feeds
    """
    feeds = Feed.active.all()
    site = get_current_site(request)
    return render(request, 'feedaggregator/export/opml.xml', {'feeds': feeds, 'site': site}, content_type="application/xhtml+xml")
