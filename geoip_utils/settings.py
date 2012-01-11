from django.conf import settings


REQUEST_IP_RESOLVER = getattr("GEOIP_REQUEST_IP_RESOLVER", "geoip_utils.utils.remote_addr_ip")

CACHE_METHOD = getattr("GEOIP_CACHE_METHOD", "GEOIP_MEMORY_CACHE")