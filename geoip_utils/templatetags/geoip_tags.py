from django import template

from ..utils import get_ip_of_request
from ..core import get_country, get_city
from ..settings import CACHE_METHOD

register = template.Library()

@register.filter()
def country_of_request(request):
    return get_country(request)

@register.filter()
def country_code_of_request(request):
    return get_country_code(request)

@register.filter()
def country_name_of_request(request):
    return get_country_name(request)

@register.filter()
def city_of_request(request):
    return get_city(request)
    
@register.filter()
def city_name_of_request(request):
    city = get_city(request)
    if city:
        return city["city"]
    
@register.filter()
def lat_lon_of_request(request):
    return get_lat_lon(request)
    
@register.filter()
def lat_of_request(request):
    return get_lat_lon(request)["lat"]

@register.filter()
def lon_of_request(request):
    return get_lat_lon(request)["lon"]
    
@register.filter()
def postal_code_of_request(request):
    city = get_city(request)
    if city:
        return city["postal_code"]
    
@register.filter()
def region_of_request(request):
    city = get_city(request)
    if city:
        return city["region"]
        
@register.filter()
def dma_code_of_request(request):
    city = get_city(request)
    if city:
        return city["dma_code"]
    
@register.filter()
def area_code_of_request(request):
    city = get_city(request)
    if city:
        return city["area_code"]
    