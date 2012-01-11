======================
GeoIp Data and helpers
======================


Install
===============

pip install django-geoip-utils==0.0.2

In your settings write::

    import geoip_utils
    GEOIP_PATH = geoip_utils.where()


This product includes GeoLite data created by MaxMind, available from http://maxmind.com/


Settings
===============

**GEOIP_REQUEST_IP_RESOLVER**

:Default: ``geoip_utils.core.remote_addr_ip``

The function used for getting the IP of the client from the request.


:Options:

* geoip_utils.utils.remote_addr_ip 
  uses the REMOTE_ADDR of the request. Good for development and standard setup
* geoip_utils.utils.x_forwarded_ip
  picks the first IP of HTTP_X_FORWARDED_FOR. This is useful for Load balancers, but could be spoofed in some cases. Amazon ELB set this reliably though
* geoip_utils.utils.real_ip
  uses the HTTP_X_REAL_IP attribute



**GEOIP_CACHE_METHOD**

:Default: ``GEOIP_MEMORY_CACHE``

The caching function used for retrieving the location.


Utils
===============

There are a few server utility functions to make the handling easier::

    from geoip_utils import core
    core.get_country(request)
    core.get_city(request)
    core.get_lat_lon(request)
    core.get_country_code(request)
    core.get_country_name(request)
    

Filters
===============

There are filters for extracting the information you need in the templates.
You need to have ``django.core.context_processors.request`` enabled in your TEMPLATE_CONTEXT_PROCESSORS::

    {% load geoip_tags %}
    {{ request|country_code_of_request }}
    {{ request|city_name_of_request }}
    {{ request|postal_code_of_request }}
    {{ request|region_of_request }}
    {{ request|dma_code_of_request }}
    {{ request|area_code_of_request }}
    {{ request|lat_of_request }}
    {{ request|lon_of_request }}
    
    
Todo
===============

* Add a management command to update the database files


