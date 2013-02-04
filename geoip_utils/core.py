try:
    from django.contrib.gis.geoip import GeoIP
except ImportError:
    from django.contrib.gis.utils import GeoIP

from .utils import get_ip_of_request
from .settings import CACHE_METHOD

geoip = GeoIP(cache=CACHE_METHOD)


def get_country(request):
    ip = get_ip_of_request(request)
    if ip:
        return geoip.country(ip)


def get_city(request):
    ip = get_ip_of_request(request)
    if ip:
        return geoip.city(ip)


def get_lat_lon(request):
    ip = get_ip_of_request(request)
    if ip:
        return geoip.lat_lon(ip)


def get_country_code(request):
    ip = get_ip_of_request(request)
    if ip:
        return geoip.country_code(ip)


def get_country_name(request):
    ip = get_ip_of_request(request)
    if ip:
        return geoip.country_name(ip)
