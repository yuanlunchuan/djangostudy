from django.conf.urls import url
from article.views import *

urlpatterns = [
  url(r'^$', index, name='index'),
  url(r'^new$', new, name='new'),
  url(r'^create$', create, name='create'),
]
