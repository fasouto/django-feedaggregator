Configuration
=============

General settings
----------------

.. setting:: FEEDAGGREGATOR_PAGE_SIZE
FEEDAGGREGATOR_PAGE_SIZE (default: 10)
  How many items display in a page

.. setting:: FEEDAGGREGATOR_TITLE
FEEDAGGREGATOR_TITLE (default: "Latest posts")
   Index page tittle
    
.. setting:: FEEDAGGREGATOR_SHOW_FULL
FEEDAGGREGATOR_SHOW_FULL (default: False)
    If set to True display all the text from the RSS feed

.. setting:: FEEDAGGREGATOR_EXCERPT_SIZE
FEEDAGGREGATOR_EXCERPT_SIZE = (default: 200)
    If `FEEDAGGREGATOR_SHOW_FULL` is False, this controls the number of words to display per item


RSS Feed settings
-----------------

These settings control generated Feeds not the ones consumed

.. setting:: FEEDAGGREGATOR_RSS_SIZE
FEEDAGGREGATOR_RSS_SIZE (default: 25)
    Number of items per RSS feed

.. setting:: FEEDAGGREGATOR_RSS_DESCRIPTION
FEEDAGGREGATOR_RSS_DESCRIPTION (default: "")
    Text to put in the feed description

Tag settings
------------
.. setting:: FEEDAGGREGATOR_TAGS_LOWERCASE
FEEDAGGREGATOR_TAGS_LOWERCASE (default: ``True``) 
    If True all the tags are converted to lowercase ``Python -> python``