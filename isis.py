#!/usr/bin/env python

from iosxe import IosXe
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
import settings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if __name__ == "__main__":
    rojter = IosXe('https://172.22.0.81:55443')
    rojter.login(settings.username, settings.password)
    print rojter.get('/api/v1/routing-svc/isis')

