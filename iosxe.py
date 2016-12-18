#!/usr/bin/env python

import requests
from requests.auth import HTTPBasicAuth
import json

class IosXe(object):
    def __init__(self, url, verify=False):
        self.url = url
        self.token = None
        self.verify = False

    def login(self, username, password):
        r = self.post('/api/v1/auth/token-services',
                      auth=HTTPBasicAuth(username, password))
        if r.status_code != 200:
            return False
        data = json.loads(r.text)
        self.token = data['token-id']
        return True

    def post(self, uri, headers = None, **kwargs):
        if not headers:
            headers = {}
        if self.token:
            headers['X-auth-token'] = self.token

        headers['Accept'] = 'application/json'
        headers['Content-Type'] = 'application/json'
        if 'auth' in kwargs:
            auth = kwargs['auth']
            r = requests.post(self.url + uri, headers=headers, auth=auth, verify=self.verify)
            return r
        data = json.dumps(kwargs['data'])
        r = requests.post(self.url + uri, data=data, headers=headers, verify=self.verify)
        return r.text

    def get(self, uri, headers=None):
        if not headers:
            headers = {}
        headers['X-auth-token'] = self.token
        headers['Accept'] = 'application/json'
        r = requests.get(self.url + uri, headers=headers, verify=self.verify)
        return r.text

if __name__ == "__main__":
    rojter = IosXe('https://172.22.0.81:55443')
    rojter.login('cisco', 'cisco')
    print rojter.get('/api/v1/global/host-name')
