'''
    Cloudforms.TaskManager
    ~~~~~~~~~~~~~~~~~~~~~~
    Task Manager

    :license: MIT, see LICENSE for more details.
'''
from Cloudforms.utils import update_params


class TaskManager(object):
    '''Manages Tasks.

    :param Cloudforms.API.Client client: an API client instance

    Example::

        import Cloudforms
        client = Cloudforms.Client()
        task_mgr = Cloudforms.TaskManager(client)
    '''
    def __init__(self, client):
        self.client = client

    def get_task(self, _id, params=None):
        '''Retrieve details about a task on the account

        :param string _id: Specifies which task the request is for
        :param dict params: response-level options (attributes, limit, etc.)
        :returns: Dictionary representing the matching task

        Example::

            # Gets a list of all tasks (returns IDs only)
            tasks = task_mgr.list_tasks({'attributes': 'id'})
            for task in tasks:
                task_details = task_mgr.get_task(task['id'])
        '''
        params = update_params(params, {'expand': 'resources'})
        return self.client.call('get', '/tasks/%s' % _id, params=params)

    def list_tasks(self, params=None):
        '''Retrieve a list of all tasks on the account

        :param dict params: response-level options (attributes, limit, etc.)
        :returns: List of dictionaries representing the matching tasks

        Example::

            # Gets a list of all tasks (returns IDs only)
            tasks = task_mgr.list_tasks({'attributes': 'id'})
        '''
        params = update_params(params, {'expand': 'resources'})
        return self.client.call('get', '/tasks', params=params)
