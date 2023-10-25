django-subdomains
=================

Subdomain helpers for the Django framework, including subdomain-based URL
routing and reversing.

Full documentation can be found here: http://django-subdomains.readthedocs.org/

Added functionality from Source repo

1. Upgrade to latest Django (4.2)
2. Enhanced settings

Settings
--------
`SUBDOMAIN_URLS_FUNCTION_PATH`: a dotted function, default to `subdomains.utils.get_subdomain_urls`
Accepts the subdomain and a default urlconf as parameters, and returns a urlconf.


Build Status
------------

.. image:: https://secure.travis-ci.org/tkaemming/django-subdomains.png?branch=master
   :target: http://travis-ci.org/tkaemming/django-subdomains

Tested on Python 2.6, 2.7, 3.4 and 3.5 on their supported Django versions from
1.4 through 1.9.
