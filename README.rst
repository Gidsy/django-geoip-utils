GeoIp Data and helpers
======================

Installation
------------

::

    pip install django-geoip-utils==0.0.2

In your settings write::

    import geoip_utils
    GEOIP_PATH = geoip_utils.where()


This product includes GeoLite data created by MaxMind, available from http://maxmind.com/


Settings
--------

GEOIP_REQUEST_IP_RESOLVER
^^^^^^^^^^^^^^^^^^^^^^^^^

:Default: ``'geoip_utils.core.remote_addr_ip'``

The function used for getting the IP of the client from the request.

:Options:

* ``'geoip_utils.utils.remote_addr_ip'``

  Uses the REMOTE_ADDR of the request. Good for development and standard setup

* ``'geoip_utils.utils.x_forwarded_ip'``

  Picks the first IP of the ``HTTP_X_FORWARDED_FOR`` request header.
  This is useful for Load balancers, but could be spoofed in some cases.
  Amazon ELB sets this reliably though.

* ``'geoip_utils.utils.real_ip'``

  Uses the HTTP_X_REAL_IP attribute

GEOIP_CACHE_METHOD
^^^^^^^^^^^^^^^^^^

:Default: ``django.contrib.gis.geoip.GeoIP.GEOIP_STANDARD``

The caching function used for retrieving the location.

:Options:

* ``django.contrib.gis.geoip.GeoIP.GEOIP_STANDARD``

  Read database from filesystem, uses least memory

* ``django.contrib.gis.geoip.GeoIP.GEOIP_MEMORY_CACHE``

  Load database into memory, faster performance but uses more memory

* ``django.contrib.gis.geoip.GeoIP.GEOIP_CHECK_CACHE``

  check for updated database.  If database has been updated, reload
  filehandle and/or memory cache. This option is not thread safe but
  is good for development.

* ``django.contrib.gis.geoip.GeoIP.GEOIP_INDEX_CACHE``

  Just cache the most frequently accessed index portion of the database,
  resulting in faster lookups than ``GEOIP_STANDARD``, but less memory
  usage than ``GEOIP_MEMORY_CACHE`` - useful for larger databases such as
  GeoIP Organization and GeoIP City. Note, for GeoIP Country, Region and
  Netspeed databases, ``GEOIP_INDEX_CACHE`` is equivalent to
  ``GEOIP_MEMORY_CACHE``.

* ``django.contrib.gis.geoip.GeoIP.GEOIP_MMAP_CACHE``

  Loads database into mmap shared memory (not available on Windows).

Utilities
=========

There are a few server utility functions to make the handling easier::

    from geoip_utils import core as geoip
    
    geoip.get_country(request)
    
    geoip.get_city(request)
    
    geoip.get_lat_lon(request)
    
    geoip.get_country_code(request)
    
    geoip.get_country_name(request)
    

Template filters
================

There are filters for extracting the information you need in the templates.
You need to have ``django.core.context_processors.request`` enabled in your
TEMPLATE_CONTEXT_PROCESSORS::

    {% load geoip_tags %}

    {{ request|country_code_of_request }}
    {{ request|city_name_of_request }}
    {{ request|postal_code_of_request }}
    {{ request|region_of_request }}
    {{ request|dma_code_of_request }}
    {{ request|area_code_of_request }}
    {{ request|lat_of_request }}
    {{ request|lon_of_request }}
    
    
TODO
====

* Add a management command to update the database files
