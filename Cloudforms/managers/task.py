'''
    Cloudforms.TaskManager
    ~~~~~~~~~~~~~~~~~~~~~~
    Task Manager

    :license: MIT, see LICENSE for more details.
'''
from time import sleep
from datetime import datetime, timedelta
from Cloudforms.utils import (
    update_params,
    normalize_object,
    normalize_collection
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

    def get(self, _id, params=None):
        '''Retrieve details about a task on the account

        :param string _id: Specifies which task the request is for
        :param dict params: response-level options (attributes, limit, etc.)
        :returns: Dictionary representing the matching task

        Example::

            # Gets a list of all tasks (returns IDs only)
            tasks = task_mgr.list({'attributes': 'id'})
            for task in tasks:
                task_details = task_mgr.get(task['id'])
        '''
        params = update_params(params, {'expand': 'resources'})
        return normalize_object(
            self.client.call('get', '/tasks/%s' % _id, params=params))

    def list(self, params=None):
        '''Retrieve a list of all tasks on the account

        :param dict params: response-level options (attributes, limit, etc.)
        :returns: List of dictionaries representing the matching tasks

        Example::

            # Gets a list of all tasks (returns IDs only)
            tasks = task_mgr.list({'attributes': 'id'})
        '''
        params = update_params(params, {'expand': 'resources'})
        return normalize_collection(
            self.client.call('get', '/tasks', params=params))

    def wait(self, _id, timeout=30, state='finished', params=None):
        '''Waits for a task to reach a certain state

        :param string state: wait until the task reaches this state
                             (case insensitive)
        :param integer timeout: operation timeout (in seconds)
        :param dict params: response-level options (attributes, limit, etc.)
        :returns bool: **True** on success, **False** on error or timeout

        Example::

            # Gets a list of all virtual servers
            vms = vs_mgr.list()
            for vm in vms:
                # Send a request to stop the virtual server
                task = vs_mgr.stop(vms.get('id'))
                # Wait for the task to finish and collect the result
                task_succeeded = task_mgr.wait(task.get('task_id'))
        '''
        deadline = datetime.now() + timedelta(seconds=timeout)
        while datetime.now() <= deadline:
            task = self.get(_id, params=params)
            if not task or not task.get('state'):
                return False
            elif task.get('state').lower() == state.lower():
                return True
            sleep(1)
        return False
