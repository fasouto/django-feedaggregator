Management commands
===================

The ``import_opml`` command
---------------------------

.. code-block:: console

    $ python manage.py import_opml http://planetpython.org/opml.xml

Import all the feed urls defined in the OPML file passed as parameter to the database. It didn't fetch the feed data, to do this run ``update_feeds``.


The ``update_feeds`` command
------------------------

.. code-block:: console

    $ python manage.py update_feeds

Update all the active feeds in the project.
