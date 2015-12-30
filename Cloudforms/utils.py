'''Cloudforms - Core classes and definitions'''
from collections import namedtuple
from requests import request
from Cloudforms.exceptions import CloudformsHTTPError

CloudformsEndpoint = namedtuple(
    'CloudformsEndpoint',
    ['username', 'password', 'host', 'secure', 'headers'])


def update_params(params, updates):
    '''Merges updates into params'''
    params = params.copy() if isinstance(params, dict) else dict()
    params.update(updates)
    return params


def returns_object(func):
    '''Returns a single object'''
    def func_wrapper(*args, **kwargs):
        '''Normalizes the object'''
        ret = func(*args, **kwargs)
        return ret if not isinstance(ret, list) else ret[0]
    return func_wrapper


def returns_collection(func):
    '''Returns a collection'''
    def func_wrapper(*args, **kwargs):
        '''Normalizes the collection'''
        ret = func(*args, **kwargs)
        return ret if isinstance(ret, list) else [ret]
    return func_wrapper


# pylint: disable=too-few-public-methods
class CloudformsBase(object):
    '''Base class that all other classes inherit from'''
    def __init__(self, endpoint, logger=None):
        self.endpoint = endpoint
        self.log = logger

    def call(self, method, path, data=None, params=None):
        '''Makes an API call'''
        # Normalize the method name for later string comparison
        method = method.lower()
        # Log our API call
        if self.log:
            self.log.info('API Call: [%s] %s://%s/api%s [%s]' % (
                method,
                'https' if self.endpoint.secure else 'http',
                self.endpoint.host,
                path,
                data
            ))
        # Make the API call
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
        # If the call was rejected, return None
        if res.status_code not in [200, 201]:
            raise CloudformsHTTPError(res.status_code, res.reason)
        # Get a proper return object
        obj = res.json()
        # With an API design rich in unnecessary complexities, we find
        # ourselves in need of a post-processor to ensure we return the
        # correct object to the consumer. Inconsistent API returns need
        # to be killed with fiya. </rant>
        if method == 'post':
            ret = obj.get('results')
        else:
            ret = obj.get('resources')
        # Fall back to returning the entire result if we couldn't
        # adequately guess what the API arbitrarily felt like returning.
        ret = ret if ret is not None else obj
        # Log our API result
        if self.log:
            self.log.info('API Result: [%s] %s://%s/api%s [%s]' % (
                method,
                'https' if self.endpoint.secure else 'http',
                self.endpoint.host,
                path,
                ret
            ))
        return ret
