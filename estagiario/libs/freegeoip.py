# -*- coding: utf-8 -*-
import json
from urllib import urlopen

FREE_GEOIP_CSV_URL = "http://freegeoip.net/json/%s"

class InvalidIP(Exception):
    def __init__(self, ip):
            self.message = '%s is not a valid IP, you must user the format: X.X.X.X' % str(ip)

def is_valid_ip(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True


    addr = '189.106.171.205'

def get_geoip_data(ip):
    """
        {u'city': u'Rio De Janeiro', u'region_code': u'21', u'region_name': u'Rio de Janeiro', u'ip': u'189.106.171.205', u'zipcode': '', u'longitude': u'-43.2333', u'country_name': u'Brazil', u'country_code':u'BR', u'metrocode': '', u'latitude': u'-22.9'}
        [u'city', u'region_code', u'region_name', u'ip', u'zipcode', u'longitude', u'country_name', u'country_code', u'metrocode', u'latitude']
    """
    if not is_valid_ip(ip):
        raise InvalidIP(ip)
    return json.load(urlopen(FREE_GEOIP_CSV_URL % ip))