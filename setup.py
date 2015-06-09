# -*- coding: utf-8 -*-
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-feedaggregator',
    version='0.2',
    packages=['feedaggregator'],
    include_package_data=True,
    description='Django app to create an RSS feeds aggregator',
    long_description=README,
    url='https://github.com/fasouto/feedaggregator/',
    install_requires=[
        'feedparser',
        'listparser',
        'django-uuslug',
        'django-taggit',
        'celery',
        'django-taggit-templatetags2'
    ],
    author='Fabio Souto',
    author_email='fabio@fabiosouto.me',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
    ],
)
