======================
GeoIp Data and helpers
======================


Install
===============

pip install django-geoip-data==0.0.1

In your settings write::

    import geoip_data
    GEOIP_PATH = geoip_data.where()


This product includes GeoLite data created by MaxMind, available from http://maxmind.com/


Configuration
===============

**GEOIP_REQUEST_IP_RESOLVER**

**Default:** geoip_data.core.remote_addr_ip
The function used for getting the IP of the client from the request.

**Options:**

* geoip_data.utils.remote_addr_ip 
  uses the REMOTE_ADDR of the request. Good for development and standard setup
* geoip_data.utils.x_forwarded_ip
  picks the first IP of HTTP_X_FORWARDED_FOR. This is useful for Load balancers, but could be spoofed in some cases. Amazon ELB set this reliably though
* geoip_data.utils.real_ip
  uses the HTTP_X_REAL_IP attribute



