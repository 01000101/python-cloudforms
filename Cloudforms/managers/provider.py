'''
    Cloudforms.ProviderManager
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    Provider Manager

    :license: MIT, see LICENSE for more details.
'''
from Cloudforms.utils import (
    update_params,
    normalize_object,
    normalize_collection
)
from Cloudforms.managers.tag import ServiceTagManager


class ProviderManager(object):
    '''Manages Providers.

    :param Cloudforms.API.Client client: an API client instance

    Example::

        import Cloudforms
        client = Cloudforms.Client()
        provider_mgr = Cloudforms.ProviderManager(client)
    '''
    def __init__(self, client):
        self.client = client
        self.tags = ServiceTagManager(client, 'providers')

    def get(self, _id, params=None):
        '''Retrieve details about a provider on the account

        :param string _id: Specifies which provider the request is for
        :param dict params: response-level options (attributes, limit, etc.)
        :returns: Dictionary representing the matching provider

        Example::

            # Gets a list of all providers (returns IDs only)
            providers = provider_mgr.list({'attributes': 'id'})
            for provider in providers:
                provider_details = provider_mgr.get(provider['id'])
        '''
        params = update_params(params, {'expand': 'resources'})
        return normalize_object(
            self.client.call('get', '/providers/%s' % _id, params=params))

    def list(self, params=None):
        '''Retrieve a list of all providers on the account

        :param dict params: response-level options (attributes, limit, etc.)
        :returns: List of dictionaries representing the matching providers

        Example::

            # Gets a list of all providers (returns IDs only)
            providers = provider_mgr.list({'attributes': 'id'})
        '''
        params = update_params(params, {'expand': 'resources'})
        return normalize_collection(
            self.client.call('get', '/providers', params=params))

    def perform_action(self, _id, action, params=None):
        '''Sends a request to perform an action on a provider

        :param string _id: Specifies which provider the request is for
        :param string action: The action to request (delete, refresh, etc.)
        :param dict params: Additional POST request data
        :returns: Task request, or Provider, dictionary object

        Example::

            # Gets a list of all providers
            for provider in provider_mgr.list():
                # Send requests to refresh all providers
                provider_mgr.perform_action(provider['id'], 'refresh')
        '''
        params = update_params(params, {'action': action})
        return normalize_object(
            self.client.call('post', '/providers/%s' % _id, data=params))

    def create(self, params=None):
        '''Creates a new provider on the account (pass-through params)

        :param dict params: Additional POST request data
        :returns: Provider dictionary object

        Example::

            # Creates a new provider using pass-through params
            provider = provider_mgr.create({
                'type': 'EmsRedhat',
                'name': 'rhevm101',
                'hostname': 'rhevm101',
                'ipaddress': '127.0.0.1',
                'credentials': {
                    'userid': 'admin',
                    'password': 'smartvm'
                }
            })
            # Refresh the provider
            provider_mgr.refresh(provider['id'])
        '''
        return normalize_object(
            self.client.call('post', '/providers', data=params))

    # pylint: disable=too-many-arguments
    def create_amazon(self, name, region,
                      access_key, secret_key,
                      params=None):
        '''Creates a new Amazon (AWS) provider on the account

        :param name string: Display name of the provider
        :param region string: AWS region (ex. us-east-1)
        :param access_key string: AWS API Access Key ID
        :param secret_key string: AWS API Access Secret Key
        :param dict params: Additional POST request data
        :returns: Provider dictionary object

        Example::

            # Creates a new Amazon (AWS) provider
            provider = provider_mgr.create_amazon(
                name='MyAWSProvider',
                region='us-east-1',
                access_key='MY4CC3SSK3Y',
                secret_key='My$Freak1shly/L0ng=S3cr3t&K3y'
            )
            # Refresh the provider
            provider_mgr.refresh(provider['id'])
        '''
        return self.create(update_params(params, {
            'type': 'ManageIQ::Providers::Amazon::CloudManager',
            'name': name,
            'provider_region': region,
            'credentials': {
                'userid': access_key,
                'password': secret_key
            }
        }))

    def delete(self, _id, params=None):
        '''Sends a request to delete a provider

        :param string _id: Specifies which provider the request is for
        :param dict params: Additional POST request data
        :returns: Task request dictionary (see TaskManager)

        Example::

            # Gets a list of all providers
            for provider in provider_mgr.list():
                # Send requests to delete all providers
                task = provider_mgr.delete(provider['id'])
                # Wait for the request to be processed
                task_mgr.wait_for_task(task.get('task_id'))
        '''
        return self.perform_action(_id, 'delete', params)

    def refresh(self, _id, params=None):
        '''Sends a request to refresh a provider

        :param string _id: Specifies which provider the request is for
        :param dict params: Additional POST request data
        :returns: JSON object with a 'success' key

        Example::

            # Gets a list of all providers
            for provider in provider_mgr.list():
                # Send requests to refresh all providers
                res = provider_mgr.refresh(provider['id'])
                if not res or not res.get('success'):
                    raise RuntimeError('An error occurred')
        '''
        return self.perform_action(_id, 'refresh', params)

    def update(self, _id, params=None):
        '''Sends a request to update a provider

        :param string _id: Specifies which provider the request is for
        :param dict params: Additional POST request data
        :returns: Provider dictionary object (with updates applied)

        Example::

            # Gets a list of all providers
            for provider in provider_mgr.list():
                # Send requests to update all providers
                provider_mgr.update(
                    provider['id'],
                    params={
                        'credentials': [{
                            'userid': 'metrics_userid',
                            'password': 'metrics_password',
                            'auth_type': 'metrics'
                        }]
                    }
                )
        '''
        return self.perform_action(_id, 'edit', params)
