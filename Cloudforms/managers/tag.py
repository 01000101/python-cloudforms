'''
    Cloudforms.TagManager
    ~~~~~~~~~~~~~~~~~~~~~~
    Tag Manager

    :license: MIT, see LICENSE for more details.
'''
from Cloudforms.utils import (
    update_params,
    normalize_object,
    normalize_collection
)


class ServiceTagManager(object):
    '''Manages Tags for Services.

    :param Cloudforms.API.Client client: an API client instance
    :param string svc: a service name to bind to
    '''
    def __init__(self, client, svc):
        self.client = client
        self.svc = svc

    def assign(self, _id, names):
        '''Assigns one or more tags to a service

        :param string _id: Specifies which service item the request is for
        :param list names: Names of tags to assign (['/my/tag', '/a/tag'])

        Example::

            # Add the tag /environment/prod to all providers
            for prov in prov_mgr.list_providers():
                prov_mgr.tags.assign(prov.get('id'), [
                    '/environment/prod'
                ])
        '''
        self.client.call('post', '/%s/%s/tags' % (self.svc, _id), data={
            'action': 'assign',
            'resources': [{'name': name} for name in names]
        })

    def unassign(self, _id, names):
        '''Un-assigns one or more tags to a service

        :param string _id: Specifies which service item the request is for
        :param list names: Names of tags to un-assign (['/my/tag', '/a/tag'])

        Example::

            # Removes the tag /environment/prod from all providers
            for prov in prov_mgr.list_providers():
                prov_mgr.tags.unassign(prov.get('id'), [
                    '/environment/prod'
                ])
        '''
        self.client.call('post', '/%s/%s/tags' % (self.svc, _id), data={
            'action': 'unassign',
            'resources': [{'name': name} for name in names]
        })


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

    def get(self, _id, params=None):
        '''Retrieve details about a tag on the account

        :param string _id: Specifies which tag the request is for
        :param dict params: response-level options (attributes, limit, etc.)
        :returns: Dictionary representing the matching tag

        Example::

            # Gets a list of all tags (returns IDs only)
            tags = tag_mgr.list({'attributes': 'id'})
            for tag in tags:
                tag_details = tag_mgr.get(tag['id'])
        '''
        params = update_params(params, {'expand': 'resources'})
        return normalize_object(
            self.client.call('get', '/tags/%s' % _id, params=params))

    def list(self, params=None):
        '''Retrieve a list of all tags on the account

        :param dict params: response-level options (attributes, limit, etc.)
        :returns: List of dictionaries representing the matching tags

        Example::

            # Gets a list of all tags (returns IDs only)
            tags = tag_mgr.list({'attributes': 'id'})
        '''
        params = update_params(params, {'expand': 'resources'})
        return normalize_collection(
            self.client.call('get', '/tags', params=params))
