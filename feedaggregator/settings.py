"""
Settings for feedaggregator project
"""
from django.conf import settings as django_settings

FEEDAGGREGATOR_PAGE_SIZE = getattr(django_settings, 'FEEDAGGREGATOR_PAGE_SIZE', 10)
FEEDAGGREGATOR_TITLE = getattr(django_settings, 'FEEDAGGREGATOR_TITLE', "Latest posts")
FEEDAGGREGATOR_SHOW_FULL = getattr(django_settings, 'FEEDAGGREGATOR_SHOW_FULL', False)
FEEDAGGREGATOR_EXCERPT_SIZE = getattr(django_settings, 'FEEDAGGREGATOR_EXCERPT_SIZE', 200)

# Own RSS feed
FEEDAGGREGATOR_RSS_SIZE = getattr(django_settings, 'FEEDAGGREGATOR_RSS_SIZE', 25)
FEEDAGGREGATOR_RSS_DESCRIPTION = getattr(django_settings, 'FEEDAGGREGATOR_RSS_DESCRIPTION', "")

# Tags
FEEDAGGREGATOR_TAGS_LOWERCASE = getattr(django_settings, 'FEEDAGGREGATOR_TAGS_LOWERCASE', True)
