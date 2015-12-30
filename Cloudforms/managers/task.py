'''
    Cloudforms.TaskManager
    ~~~~~~~~~~~~~~~~~~~~~~
    Task Manager

    :license: MIT, see LICENSE for more details.
'''
from Cloudforms.utils import (
    update_params,
    returns_object,
    returns_collection
)


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

    @returns_object
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

    @returns_collection
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

    def wait_for_task(self, _id, state='finished', params=None):
        '''Waits for a task to reach a certain state

        :param string state: wait until the task reaches this state
                             (case insensitive)
        :param dict params: response-level options (attributes, limit, etc.)
        :returns bool: **True** on success, **False** on error or timeout

        Example::

            # Gets a list of all virtual servers
            vms = vs_mgr.list_instances()
            for vm in vms:
                # Send a request to stop the virtual server
                task = vs_mgr.stop_instance(vms.get('id'))
                # Wait for the task to finish and collect the result
                task_succeeded = task_mgr.wait_for_task(task.get('task_id'))
        '''
        while True:
            task = self.get_task(_id, params=params)
            if not task or not task.get('state'):
                return False
            elif task.get('state').lower() == state.lower():
                return True
