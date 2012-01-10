from django import template
from django.contrib.gis.utils import GeoIP
from ..utils import get_ip_of_request
from ..settings import CACHE_METHOD

register = template.Library()


@register.filter()
def get_country(request):
    ip = get_ip_of_request(request)
    if ip:
        g = GeoIP(cache=CACHE_METHOD)
        return g.country(ip)
    return None


@register.filter()
def get_country(value):
    ip = get_ip_of_request(request)
    if ip:
        g = GeoIP(cache=CACHE_METHOD)
        return g.city(ip)
    return None