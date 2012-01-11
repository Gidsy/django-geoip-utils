from django.utils.importlib import import_module
from django.core.exceptions import ImproperlyConfigured
from .settings import REQUEST_IP_RESOLVER


def get_ip_of_request(request):
    """
        This is the default way to get the IP from the request,
        Other resolvers can be hooked up using the settings
    """
    try:
        (module, attribute) = REQUEST_IP_RESOLVER.rsplit(".", 1)
        ip_resolver_module = import_module(module)
        ip_resolver = getattr(ip_resolver_module, attribute)
    except ImportError:
        raise ImproperlyConfigured("Please specify a valid GEOIP_REQUEST_IP_RESOLVER module. "
                                    "Could not find %s " % module)
    except AttributeError:
        raise ImproperlyConfigured("Please specify a valid GEOIP_REQUEST_IP_RESOLVER "
                                   "function. Could not find %s function in module %s" % (attribute, module))

    return ip_resolver(request)


def remote_addr_ip(request):
    """
    This is for the development setup.
    """
    ip_address = None
    if request.META.has_key('REMOTE_ADDR'):
        ip_address = request.META.get('REMOTE_ADDR')
    return ip_address


def x_forwarded_ip(request):
    """
    Amazon ELB stores the IP in the HTTP_X_FORWARDED_FOR META attribute.
    It is realiably the first one of the IP adresses sent and can be trusted (eg.: cannot be spoofed)
    Warning: This might not be true for other load balancers

    This function assumes that your Nginx is configured with:
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    """
    ip_address = None
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip_address_array = request.META.get('HTTP_X_FORWARDED_FOR').split(",")
        if ip_address_array:
            ip_address = ip_address_array[0]
    return ip_address


def real_ip(request):
    """
    Behind a Wsgi (Nginx) server.
    """
    ip_address = None
    if request.META.has_key('HTTP_X_REAL_IP'):
        ip_address = request.META.get('HTTP_X_REAL_IP')
    return ip_address
