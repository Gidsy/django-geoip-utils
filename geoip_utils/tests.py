import unittest
from templatetags import geoip_tags

class GeoIpDataTestCase(unittest.TestCase):
    def test_country(self):
        request = object()
        request.META = {'REMOTE_ADDR': "1.1.1.1"}
        country = geoip_tags.country_of_request(request)

if __name__ == '__main__':
    unittest.main()
