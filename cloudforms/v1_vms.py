'''Interface for /api/vms'''
from .utils import CloudformsBase, update_params
from .v1_tags import CloudformsServiceTags


class CloudformsVMS(CloudformsBase):
    '''VMS interface'''
    def __init__(self, endpoint, logger):
        CloudformsBase.__init__(self, endpoint, logger)
        self.tags = CloudformsServiceTags('vms', endpoint, logger)

    def list(self, _id='', params=None):
        '''Get one or more VM objects
           inputs:
             _id (string): Specifies a VM by its ID
             params (dict): Additional GET query parameters
        '''
        params = update_params(params, {'expand': 'resources'})
        return self.request('get', '/vms/%s' % _id, params=params)

    def set_owner(self, _id, owner):
        '''Sets the owner of a VM
           inputs:
             _id (string): Specifies which VM (by ID) to set the owner of
             owner (string): Name of the new VM owner
        '''
        return self.request('post', '/vms/%s' % _id, data={
            'action': 'set_owner',
            'resource': {
                'owner': owner
            }
        })

    def add_event(self, _id, evt_type, evt_msg):
        '''Adds an event to a VM
           inputs:
             _id (string): Specifies which VM (by ID) to add an event to
             evt_type (string): Event type
             evt_msg (string): Event message
        '''
        return self.request('post', '/vms/%s' % _id, data={
            'action': 'add_event',
            'resource': {
                'event_type': evt_type,
                'event_message': evt_msg
            }
        })

    def add_lifecycle_event(self, _id, evt, status, msg, created_by):
        '''Adds a lifecycle event to a VM
           inputs:
             _id (string): Specifies which VM (by ID) to add a lifecycle event
             evt (string): Event name
             status (string): Event status
             msg (string) Message about the event
             created_by (string): User name
        '''
        return self.request('post', '/vms/%s' % _id, data={
            'action': 'add_lifecycle_event',
            'resource': {
                'event': evt,
                'status': status,
                'message': msg,
                'created_by': created_by
            }
        })

    def scan(self, _id, params=None):
        '''Scans a VM
           inputs:
             _id (string): Specifies which VM (by ID) to scan
             params (dict): Additional POST parameters
        '''
        params = update_params(params, {'action': 'scan'})
        return self.request('post', '/vms/%s' % _id, data=params)

    def start(self, _id, params=None):
        '''Starts a VM
           inputs:
             _id (string): Specifies which VM (by ID) to start
             params (dict): Additional POST parameters
        '''
        params = update_params(params, {'action': 'start'})
        return self.request('post', '/vms/%s' % _id, data=params)

    def stop(self, _id, params=None):
        '''Stops a VM
           inputs:
             _id (string): Specifies which VM (by ID) to stop
             params (dict): Additional POST parameters
        '''
        params = update_params(params, {'action': 'stop'})
        return self.request('post', '/vms/%s' % _id, data=params)

    def suspend(self, _id, params=None):
        '''Suspends a VM
           inputs:
             _id (string): Specifies which VM (by ID) to suspend
             params (dict): Additional POST parameters
        '''
        params = update_params(params, {'action': 'suspend'})
        return self.request('post', '/vms/%s' % _id, data=params)

    def delete(self, _id):
        '''Deletes a VM
           inputs:
             _id (string): Specifies which VM (by ID) to delete
        '''
        return self.request('delete', '/vms/%s' % _id)
