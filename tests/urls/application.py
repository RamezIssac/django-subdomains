# try:
from django.urls import re_path as url
# except ImportError:
#     from django.conf.urls.defaults import patterns, url  # noqa

from tests.urls.default import urlpatterns as default_patterns
from tests.views import view


urlpatterns = default_patterns + (
    url(r'^view/$', view=view, name='view'),
    url(r'^application/$', view=view, name='application'),
)
