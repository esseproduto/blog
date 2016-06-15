#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'EsseProduto'
SITENAME = ''
SITEURL = 'http://localhost:7000'

PATH = 'content'
STATIC_PATHS = ['blog', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{slug}'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt-br'
LOCALE = ('pt_BR')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Sobre', 'http://esseproduto.com.br/site/sobre'),
         ('Assine nossa newsletter', 'http://esseproduto.com.br/site/newsletter'),
         ('Contato', 'http://esseproduto.com.br/site/contato'),
         ('Tags', '/tags/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Pagination
DEFAULT_PAGINATION = 3
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = 'authors/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORYS_URL = 'categories/'
CATEGORYS_SAVE_AS = 'categories/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Following items are often useful when publishing
DISQUS_SITENAME = "esseproduto"
GOOGLE_ANALYTICS = "UA-71341389-2"

# THEME SPECIFIC
WELCOME_MESSAGE = 'Welcome to {}'.format(SITENAME)
MENU_LINKS = (
    ('EsseProduto', 'http://esseproduto.com.br'),
)
DESCRIPTION = 'Confiabilidade através de prova social na aquisição de produtos digitais'
THEME = 'pelican-semantic-ui'
TWITTER_USERNAME = 'esseproduto'
