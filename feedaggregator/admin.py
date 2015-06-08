# -*- coding: utf-8 -*-
from django.contrib import admin

from feedaggregator.models import Feed, Item


class FeedAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'updated_on', 'is_active')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Feed, FeedAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'feed', 'is_active', 'slug')

admin.site.register(Item, ItemAdmin)
