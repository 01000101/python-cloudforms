'''Interface for /api/providers'''
from .utils import CloudformsBase, update_params
from .v1_tags import CloudformsServiceTags


class CloudformsProviders(CloudformsBase):
    '''Providers interface'''
    def __init__(self, endpoint, logger):
        CloudformsBase.__init__(self, endpoint, logger)
        self.tags = CloudformsServiceTags('providers', endpoint, logger)

    def list(self, _id='', params=None):
        '''Get one or more provider objects
           inputs:
             _id (string): Specifies a provider by its ID
             params (dict): Additional GET query parameters
        '''
        params = update_params(params, {'expand': 'resources'})
        return self.request('get', '/providers/%s' % _id, params=params)

    def refresh(self, _id, params=None):
        '''Refreshes a provider relationships
           inputs:
             _id (string): Specifies a provider by its ID
             params (dict): Additional POST parameters
        '''
        params = update_params(params, {'action': 'refresh'})
        return self.request('post', '/providers/%s' % _id, data=params)

    def refresh_all(self):
        '''Refreshes all provider relationships'''
        provs = self.list(params={'attributes': 'id'})
        for prov in provs:
            if prov.get('id'):
                self.refresh(prov.get('id'))
