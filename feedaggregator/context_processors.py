# -*- coding: utf-8 -*-

from django.conf import settings

from feedaggregator.settings import FEEDAGGREGATOR_TITLE, FEEDAGGREGATOR_SHOW_FULL, FEEDAGGREGATOR_EXCERPT_SIZE


def feedaggregator_settings(request):
    return {
        "FEEDAGGREGATOR_TITLE": FEEDAGGREGATOR_TITLE, 
        "FEEDAGGREGATOR_SHOW_FULL": FEEDAGGREGATOR_SHOW_FULL,
        "FEEDAGGREGATOR_EXCERPT_SIZE": FEEDAGGREGATOR_EXCERPT_SIZE
    }
    