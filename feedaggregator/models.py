# -*- coding: utf-8 -*-

"""
django-feedaggregator models

"""

from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

from taggit.managers import TaggableManager
from uuslug import uuslug

from feedaggregator.managers import FeedManager, ItemManager


@python_2_unicode_compatible
class Feed(models.Model):
    """
    Represents a feed in RSS, or any other format.
    """
    title = models.CharField(_("title"), max_length=255, default="<Untitled>")
    feed_url = models.CharField(_("url"), unique=True, blank=False, max_length=500)
    site_url = models.URLField(_("site url"), blank=True)
    description = models.TextField(_("description"), blank=True)
    updated_on = models.DateTimeField(_("date published"), blank=True, null=True)
    slug = models.SlugField(unique=True)

    # Meta
    date_added = models.DateTimeField(_("added on"), auto_now_add=True)
    date_modified = models.DateTimeField(_("modified on"), auto_now=True)
    is_active = models.BooleanField(_("active"), blank=True, default=True)

    # Managers
    active = FeedManager()
    objects = models.Manager()

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self, max_length=50)
        super(Feed, self).save(*args, **kwargs)

    @property
    def is_new(self):
        return self.updated_on is None

    @property
    def has_items(self):
        return Item.active.filter(feed=self).exists()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('feedaggregator:feed_detail', args=[self.slug])


@python_2_unicode_compatible
class Item(models.Model):
    """
    Represents an item on a Feed
    """
    feed = models.ForeignKey(Feed)
    title = models.CharField(_("title"), max_length=255, default="<Untitled>")
    link = models.URLField(_("url"), max_length=500)
    guid = models.CharField(_("global unique identifier"), max_length=500, blank=True, null=True)
    description = models.TextField(_("description"), blank=True)
    published_on = models.DateTimeField(_("date published"), blank=True, null=True)
    authors = models.ManyToManyField('Author', blank=True)
    tags = TaggableManager()
    slug = models.SlugField(unique=True)

    # Meta
    date_added = models.DateTimeField(_("added on"), auto_now_add=True)
    date_modified = models.DateTimeField(_("modified on"), auto_now=True)
    is_active = models.BooleanField(_("active"), blank=True, default=True)

    # Managers
    active = ItemManager()
    objects = models.Manager()

    class Meta:
        ordering = ['-published_on']

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self, max_length=50)
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('feedaggregator:item_detail', kwargs={"slug": self.slug})


@python_2_unicode_compatible
class Author(models.Model):
    """
    Represents a writer of an item
    """
    name = models.CharField(_("name"), max_length=255, blank=True, default="<Unknown>")
    profile_url = models.URLField(_("profile"), blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self, max_length=50)
        super(Author, self).save(*args, **kwargs)
