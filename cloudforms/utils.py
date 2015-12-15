'''Cloudforms - Core classes and definitions'''
from collections import namedtuple
from requests import request

CloudformsEndpoint = namedtuple(
    'CloudformsEndpoint',
    ['username', 'password', 'host', 'secure', 'headers'])


def update_params(params, updates):
    '''Merges updates into params'''
    params = params.copy() if isinstance(params, dict) else dict()
    params.update(updates)
    return params


class CloudformsBase(object):
    '''Base class that all other classes inherit from'''
    def __init__(self, endpoint, logger=None):
        self.endpoint = endpoint
        self.log = logger

    def request(self, method, path, data=None, params=None):
        '''Makes an API call'''
        if self.log:
            self.log.info('API Call: [%s] %s://%s:%s@%s/api%s [%s]' % (
                method,
                'https' if self.endpoint.secure else 'http',
                self.endpoint.username,
                self.endpoint.password,
                self.endpoint.host,
                path,
                data
            ))
        res = request(
            method,
            '%s://%s/api%s' % (
                'https' if self.endpoint.secure else 'http',
                self.endpoint.host, path
            ),
            auth=(self.endpoint.username, self.endpoint.password),
            headers=self.endpoint.headers,
            json=data,
            params=params,
            verify=False)
        if res.status_code not in [200, 201]:
            return dict()
        else:
            obj = res.json()
            self.log.debug('call_res: %s', obj)
            return obj if not obj.get('resources') else obj.get('resources')
