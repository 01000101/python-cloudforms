'''Interface for /api/<service>/<id>/tags'''
from .utils import CloudformsBase, update_params


class CloudformsServiceTags(CloudformsBase):
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

    def assign(self, _id='', category=None, tagname=None):
        '''Assigns a tag to the service object
           inputs:
             _id (string): Specifies which service object (by ID) to update
             category (string): Tag category (ex: "mycategory")
             tagname (string): Tag name (ex: "mytag")
        '''
        return self.request('post', self.path % _id, data={
            'action': 'assign',
            'resources': [{
                'category': category,
                'name': tagname
            }]
        })

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

    def assign_by_href(self, _id='', href=None):
        '''Assigns a tag (by href) to the service object
           inputs:
             _id (string): Specifies which service object (by ID) to update
             href (string): Tag (ex: "https://hostname/api/services/1/tags/49")
        '''
        return self.request('post', self.path % _id, data={
            'action': 'assign',
            'resources': [{
                'href': href
            }]
        })

    def unassign(self, _id='', category=None, tagname=None):
        '''Un-assigns a tag to the service object
           inputs:
             _id (string): Specifies which service object (by ID) to update
             category (string): Tag category (ex: "mycategory")
             tagname (string): Tag name (ex: "mytag")
        '''
        return self.request('post', self.path % _id, data={
            'action': 'unassign',
            'resources': [{
                'category': category,
                'name': tagname
            }]
        })

    def unassign_by_name(self, _id='', tagname=None):
        '''Un-assigns a tag (by name) to the service object
           inputs:
             _id (string): Specifies which service object (by ID) to update
             tagname (string): Tag name (ex: "/managed/mycategory/mytag")
        '''
        return self.request('post', self.path % _id, data={
            'action': 'unassign',
            'resources': [{
                'name': tagname
            }]
        })

    def unassign_by_href(self, _id='', href=None):
        '''Un-assigns a tag (by href) to the service object
           inputs:
             _id (string): Specifies which service object (by ID) to update
             href (string): Tag (ex: "https://hostname/api/services/1/tags/49")
        '''
        return self.request('post', self.path % _id, data={
            'action': 'unassign',
            'resources': [{
                'href': href
            }]
        })
