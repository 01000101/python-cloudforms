'''
    Cloudforms.TagManager
    ~~~~~~~~~~~~~~~~~~~~~~
    Tag Manager

    :license: MIT, see LICENSE for more details.
'''
from Cloudforms.utils import (
    update_params,
    returns_object,
    returns_collection
)


class TagManager(object):
    '''Manages Tags.

    :param Cloudforms.API.Client client: an API client instance

    Example::

        import Cloudforms
        client = Cloudforms.Client()
        tag_mgr = Cloudforms.TagManager(client)
    '''
    def __init__(self, client):
        self.client = client

    @returns_object
    def get_tag(self, _id, params=None):
        '''Retrieve details about a tag on the account

        :param string _id: Specifies which tag the request is for
        :param dict params: response-level options (attributes, limit, etc.)
        :returns: Dictionary representing the matching tag

        Example::

            # Gets a list of all tags (returns IDs only)
            tags = tag_mgr.list_tags({'attributes': 'id'})
            for tag in tags:
                tag_details = tag_mgr.get_tag(tag['id'])
        '''
        params = update_params(params, {'expand': 'resources'})
        return self.client.call('get', '/tags/%s' % _id, params=params)

    @returns_collection
    def list_tags(self, params=None):
        '''Retrieve a list of all tags on the account

        :param dict params: response-level options (attributes, limit, etc.)
        :returns: List of dictionaries representing the matching tags

        Example::

            # Gets a list of all tags (returns IDs only)
            tags = tag_mgr.list_tags({'attributes': 'id'})
        '''
        params = update_params(params, {'expand': 'resources'})
        return self.client.call('get', '/tags', params=params)
