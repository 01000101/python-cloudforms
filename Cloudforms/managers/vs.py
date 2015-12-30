'''
    Cloudforms.VSManager
    ~~~~~~~~~~~~~~~~~~~~
    VS Manager (abstracts virtual machines and cloud instances)

    :license: MIT, see LICENSE for more details.
'''
from Cloudforms.utils import (
    update_params,
    returns_object,
    returns_collection
)


class VSManager(object):
    '''Manages Virtual Servers.

    :param Cloudforms.API.Client client: an API client instance

    Example::

        import Cloudforms
        client = Cloudforms.Client()
        vs_mgr = Cloudforms.VSManager(client)
    '''
    def __init__(self, client):
        self.client = client

    @returns_object
    def get_instance(self, _id, params=None):
        '''Retrieve details about a virtual server on the account

        :param string _id: Specifies which virtual server the request is for
        :param dict params: response-level options (attributes, limit, etc.)
        :returns: Dictionary representing the matching virtual server

        Example::

            # Gets a list of all virtual server instances (returns IDs only)
            instances = vs_mgr.list_instances({'attributes': 'id'})
            for instance in instances:
                vs_details = vs_mgr.get_instance(instance['id'])
        '''
        params = update_params(params, {'expand': 'resources'})
        return self.client.call('get', '/vms/%s' % _id, params=params)

    @returns_collection
    def list_instances(self, params=None):
        '''Retrieve a list of all virtual servers on the account

        :param dict params: response-level options (attributes, limit, etc.)
        :returns: List of dictionaries representing the matching
                  virtual server

        Example::

            # Gets a list of all virtual server instances (returns IDs only)
            instances = vs_mgr.list_instances({'attributes': 'id'})
        '''
        params = update_params(params, {'expand': 'resources'})
        return self.client.call('get', '/vms', params=params)

    @returns_object
    def perform_action(self, _id, action, params=None):
        '''Sends a request to perform an action on a virtual server

        :param string _id: Specifies which virtual server the request is for
        :param string action: The action to request (start, stop, suspend, etc.)
        :param dict params: Additional POST request data
        :returns: Task request dictionary (see TaskManager)

        Example::

            # Gets a list of all virtual server instances
            for vsi in vs_mgr.list_instances():
                # Send requests to start all virtual server instances
                vs_mgr.perform_action(vsi['id'], 'start')
        '''
        params = update_params(params, {'action': action})
        return self.client.call('post', '/vms/%s' % _id, data=params)

    @returns_object
    def start_instance(self, _id, params=None):
        '''Sends a request to start a virtual server

        :param string _id: Specifies which virtual server the request is for
        :param dict params: Additional POST request data
        :returns: Task request dictionary (see TaskManager)

        Example::

            # Gets a list of all virtual server instances
            for vsi in vs_mgr.list_instances():
                # Send requests to start all virtual server instances
                vs_mgr.start_instance(vsi['id'])
        '''
        return self.perform_action(_id, 'start', params)

    @returns_object
    def stop_instance(self, _id, params=None):
        '''Sends a request to stop a virtual server

        :param string _id: Specifies which virtual server the request is for
        :param dict params: Additional POST request data
        :returns: Task request dictionary (see TaskManager)

        Example::

            # Gets a list of all virtual server instances
            for vsi in vs_mgr.list_instances():
                # Send requests to stop all virtual server instances
                vs_mgr.stop_instance(vsi['id'])
        '''
        return self.perform_action(_id, 'stop', params)

    @returns_object
    def suspend_instance(self, _id, params=None):
        '''Sends a request to suspend a virtual server

        :param string _id: Specifies which virtual server the request is for
        :param dict params: Additional POST request data
        :returns: Task request dictionary (see TaskManager)

        Example::

            # Gets a list of all virtual server instances
            for vsi in vs_mgr.list_instances():
                # Send requests to suspend all virtual server instances
                vs_mgr.suspend_instance(vsi['id'])
        '''
        return self.perform_action(_id, 'suspend', params)

    @returns_object
    def delete_instance(self, _id, params=None):
        '''Sends a request to delete a virtual server

        :param string _id: Specifies which virtual server the request is for
        :param dict params: Additional POST request data
        :returns: Task request dictionary (see TaskManager)

        Example::

            # Gets a list of all virtual server instances
            for vsi in vs_mgr.list_instances():
                # Send requests to delete all virtual server instances
                vs_mgr.delete_instance(vsi['id'])
        '''
        return self.perform_action(_id, 'delete', params)
