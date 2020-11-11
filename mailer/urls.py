#-*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.views.decorators.cache import cache_page

from .views import IndexView

urlpatterns = [
    url(r'^$', cache_page(60*60)(IndexView.as_view()), name="index"),
]
