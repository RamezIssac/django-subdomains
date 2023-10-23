# try:
from django.urls import re_path as url
# except ImportError:
#     from django.conf.urls.defaults import patterns, url  # noqa

from tests.views import view


urlpatterns =(
    url(r'^$', view=view, name='home'),
    url(r'^example/$', view=view, name='example'),
)
