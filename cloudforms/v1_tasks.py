'''Interface for /api/tasks'''
from time import sleep
from .utils import CloudformsBase, update_params


class CloudformsTasks(CloudformsBase):
    '''Tasks interface'''
    def __init__(self, endpoint, logger):
        CloudformsBase.__init__(self, endpoint, logger)

    def list(self, _id='', params=None):
        '''Get one or more task objects
           inputs:
             _id (string): Specifies a task by its ID
             params (dict): Additional GET query parameters
        '''
        params = update_params(params, {'expand': 'resources'})
        return self.request('get', '/tasks/%s' % _id, params=params)

    def wait(self, _id, state='finished', timeout=240, params=None):
        '''Polls a task until it reaches a specified state
           inputs:
             _id (string): Specifies a task by its ID
             state (string): State to wait for (case insensitive)
             timeout (integer): Timeout, in seconds, until fail
             params (dict): Additional GET query parameters
        '''
        for _ in range(timeout):
            task = self.list(_id, params={'attributes': 'id,state'})
            if task.get('state', '').lower() == state.lower():
                return self.list(_id, params=params)
            sleep(1)
        raise RuntimeError('Timeout waiting for task [%s] '
                           'to reach state [%s]' % (_id, state))
