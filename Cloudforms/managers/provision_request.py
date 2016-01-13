'''
    Cloudforms.ProvisionRequestManager
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Provision Request Manager

    :license: MIT, see LICENSE for more details.
'''
from Cloudforms.utils import (
    update_params,
    normalize_object,
    normalize_collection
)


class ProvisionRequestManager(object):
    '''Manages Provision Requests.

    :param Cloudforms.API.Client client: an API client instance

    Example::

        import Cloudforms
        client = Cloudforms.Client()
        preq_mgr = Cloudforms.ProvisionRequestManager(client)
    '''
    def __init__(self, client):
        self.client = client

    def get(self, _id, params=None):
        '''Retrieve details about a provision request on the account

        :param string _id: Specifies which provision request the request is for
        :param dict params: response-level options (attributes, limit, etc.)
        :returns: Dictionary representing the matching provision request

        Example::

            # Gets a list of all provision requests (returns IDs only)
            preqs = preq_mgr.list({'attributes': 'id'})
            for preq in preqs:
                preq_details = preq_mgr.get(preq['id'])
        '''
        params = update_params(params, {'expand': 'resources'})
        return normalize_object(
            self.client.call('get', '/provision_requests/%s' %
                             _id, params=params))

    def list(self, params=None):
        '''Retrieve a list of all provision requests on the account

        :param dict params: response-level options (attributes, limit, etc.)
        :returns: List of dictionaries representing the
                  matching provision requests

        Example::

            # Gets a list of all provision requests (returns IDs only)
            preqs = preq_mgr.list({'attributes': 'id'})
        '''
        params = update_params(params, {'expand': 'resources'})
        return normalize_collection(
            self.client.call('get', '/provision_requests', params=params))

    def perform_action(self, _id, action, params=None):
        '''Sends a request to perform an action on a provision request

        :param string _id: Specifies which provision request the request is for
        :param string action: The action to request (delete, refresh, etc.)
        :param dict params: Additional POST request data
        :returns: ProvisionRequest dictionary object
        '''
        params = update_params(params, {'action': action})
        return normalize_object(
            self.client.call('post', '/provision_requests/%s' %
                             _id, data=params))

    def create(self, params=None):
        '''Creates a new provision request on the account

        :param dict params: Additional POST request data
        :returns: ProvisionRequest dictionary object
        '''
        params = update_params(params, {'action': 'create'})
        return normalize_object(
            self.client.call('post', '/provision_requests', data=params))

    def wait(self, _id, request_state='finished', params=None):
        '''Waits for a provision request to reach a certain request_state

        :param string request_state: wait until the provision request reaches
                                     this request_state (case insensitive)
        :param dict params: response-level options (attributes, limit, etc.)
        :returns bool: **True** on success, **False** on error or timeout
        '''
        while True:
            preq = self.get(_id, params=params)
            if not preq or not preq.get('request_state'):
                return False
            elif preq.get('request_state').lower() == request_state.lower():
                return True
