#!/usr/bin/env python

from iosxe import IosXe
import settings
import json

if __name__ == "__main__":
    rojter = IosXe('https://172.22.0.81:55443')
    rojter.login(settings.username, settings.password)
    data = {'routing-protocol-id': '20514'}
    print rojter.post('/api/v1/routing-svc/bgp', data=data)
