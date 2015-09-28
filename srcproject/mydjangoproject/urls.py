"""mydjangoproject URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from webapp import views as myViews

urlpatterns = [
	# url(r'^about$', 'webapp.views.home', name='about'),
    
    url(r'^register$', 'webapp.views.get_name', name='get_name'),

    url(r'^newresource$', 'webapp.views.add_resource', name='add_resource'),

	url(r'^$', myViews.home, name='home'),

	# url(r'^$', myViews.home, name='home'),

    url(r'^admin/', include(admin.site.urls)),
]

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

