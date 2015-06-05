Installation
============

1. Install the package from pip:

.. code-block:: python

    pip install django-feedaggregator

2. Add ``feedaggregator``,  ``taggit`` and  ``taggit_templatetags2`` to INSTALLED_APPS in your settings.py:

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'feedaggregator',
        'taggit',
        'taggit_templatetags2'
    )


3. Add feedaggregator urls:

.. code-block:: python

    urlpatterns = patterns('',
        ...,
        url(r'^feedaggregator/', include('feedaggregator.urls', namespace='feedaggregator')),
    )

4. Migrate the database

.. code-block:: python

    python manage.py migrate


Done! You're good to go.



