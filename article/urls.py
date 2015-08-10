"""article URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import display_homepage, display_article
from article_db.models import *

urlpatterns = patterns('',
	url(r'^$',display_homepage),
	#url(r'^1$',display_article,{'id': '1'}),
	url(r'^(?P<id>[0-9])/$',display_article),
    url(r'^admin/', include(admin.site.urls)),
)
