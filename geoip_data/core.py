import os
from django.contrib.gis.utils import GeoIP

def get_country(request):
    ip = get_ip_of_request(request)
    if ip:
        g = GeoIP(cache=CACHE_METHOD)
        return g.country(ip)
    return None
    
    
def get_city(request):
    ip = get_ip_of_request(request)
    if ip:
        g = GeoIP(cache=CACHE_METHOD)
        return g.city(ip)
    return None


def get_lat_lon(request):
    ip = get_ip_of_request(request)
    if ip:
        g = GeoIP(cache=CACHE_METHOD)
        return g.lat_lon(ip)
    return None
    
    
def get_country_code(request):
    ip = get_ip_of_request(request)
    if ip:
        g = GeoIP(cache=CACHE_METHOD)
        return g.country_code(ip)
    return None
    
    
def get_country_name(request):
    ip = get_ip_of_request(request)
    if ip:
        g = GeoIP(cache=CACHE_METHOD)
        return g.country_name(ip)
    return None
    

def where():
    f = os.path.split(__file__)[0]
    return os.path.abspath(os.path.join(f, 'data'))
    
    
if __name__ == '__main__':
    print where()