from django.conf import settings
from django.urls import get_callable

SUBDOMAIN_URLS_FUNCTION_PATH = getattr(settings, 'SUBDOMAIN_URLS_FUNCTION', 'subdomains.utils.get_subdomain_urls')


def get_lazy_urls():
    return get_callable(SUBDOMAIN_URLS_FUNCTION_PATH)

SUBDOMAIN_URLS_FUNCTION = get_callable(SUBDOMAIN_URLS_FUNCTION_PATH)
