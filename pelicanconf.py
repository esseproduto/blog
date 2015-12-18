#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'EsseProduto'
SITENAME = 'Blog EsseProduto'
SITEURL = 'http://localhost:7000'

PATH = 'content'
STATIC_PATHS = ['blog', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{slug}'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Following items are often useful when publishing
DISQUS_SITENAME = "esseproduto"
GOOGLE_ANALYTICS = "UA-71341389-2"

# THEME SPECIFIC
MENU_LINKS = (
    ('EsseProduto', 'http://esseproduto.com.br'),
)
DESCRIPTION = 'Confiabilidade através de prova social na aquisição de produtos digitais'
THEME = 'pelican-semantic-ui'
TWITTER_USERNAME = 'esseproduto'
