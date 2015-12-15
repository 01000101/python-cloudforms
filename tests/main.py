'''Red Hat Cloudforms REST API interface'''
import logging
from cloudforms import Cloudforms

# Set our logging format
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s [%(funcName)s():%(lineno)d] %(message)s'
)


def test_tasks(api):
    '''Performs non-destructive tasks tests'''
    api.tasks.list()


def test_vms(api):
    '''Performs non-destructive VMs tests'''
    objs = api.vms.list()
    for obj in objs:
        api.vms.tags.list(obj.get('id'))
#        tags_obj = api.vms.tags.list(obj.get('id'))
#        tags = []
#        for tag_obj in tags_obj:
#            tags.append(tag_obj.get('name'))
#        if '/managed/environment/prod' in tags:
#            if '/managed/challenges/foundit' in tags:
#                logging.warn('Tag "foundit" is already assigned to '
#                             'VM %s. Skipping...', obj.get('id'))
#            else:
#                logging.info('Assigning tag "foundit" to VM %s', obj.get('id'))
#                api.vms.tags.assign_by_name(obj.get('id'),
#                                            '/managed/challenges/foundit')


def test_providers(api):
    '''Performs non-destructive provider tests'''
    api.providers.list()
    api.providers.refresh_all()


def main():
    '''Entry point'''
    logging.info('Starting Cloudforms API tests')
    api = Cloudforms(
        host='192.168.122.99',
        password='95RyXaR1OA5q',
        logger=logging)

    logging.info('Test tasks interface')
    test_tasks(api)

    logging.info('Test vms interface')
    test_vms(api)

    logging.info('Test providers interface')
    test_providers(api)


if __name__ == '__main__':
    main()
