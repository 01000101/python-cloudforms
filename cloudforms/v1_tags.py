'''Interface for /api/<service>/<id>/tags'''
from .utils import CloudformsBase, update_params


class CloudformsTags(CloudformsBase):
    '''Tags interface'''
    def __init__(self, service, endpoint, logger):
        self.service = service
        self.path = '/' + self.service + '/%s/tags'
        CloudformsBase.__init__(self, endpoint, logger)

    def list(self, _id='', params=None):
        '''Get one or more tags for a given service object
           inputs:
             _id (string): Specifies a service object by its ID
             params (dict): Additional GET query parameters
        '''
        params = update_params(params, {'expand': 'resources'})
        return self.request('get', self.path % _id, params=params)

    def assign_by_name(self, _id='', tagname=None):
        '''Assigns a tag (by name) to the service object
           inputs:
             _id (string): Specifies which service object (by ID) to update
             tagname (string): Tag name (ex: "/managed/mycategory/mytag")
        '''
        return self.request('post', self.path % _id, data={
            'action': 'assign',
            'resources': [{
                'name': tagname
            }]
        })
