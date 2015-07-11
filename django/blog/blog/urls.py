"""blog URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^htmlview/(\d+)$','htmlview.views.html_view'),

	url(r'^blogbase$','blogbase.views.blog_posts',name='index'),
	url(r'^(\d+)$','blogbase.views.post',name='post'),
    
    url(r'^votes$','votes.views.votes_view', name='votes'),
    url(r'^votes/(\d+)$','votes.views.vote_view', name='vote'),
    url(r'^votes/for/(\d+)$','votes.views.vote_vote', name='vote_for'),

    url(r'^message$','testform.views.form_view'),
    
    url(r'^admin/', include(admin.site.urls)),
]