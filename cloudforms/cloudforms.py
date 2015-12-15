'''Cloudforms public library interface'''
from .utils import CloudformsBase, CloudformsEndpoint
from .v1_providers import CloudformsProviders
from .v1_tasks import CloudformsTasks
from .v1_vms import CloudformsVMS


class Cloudforms(CloudformsBase):
    '''Public interface to the library'''
    # pylint: disable=too-many-arguments
    def __init__(self, host='127.0.0.1', secure_host=True,
                 username='admin', password='smartvm',
                 logger=None):
        endpoint = CloudformsEndpoint(
            host=host,
            secure=secure_host,
            username=username,
            password=password,
            headers={'Content-Type': 'application/json',
                     'Accept': 'application/json'}
        )

        CloudformsBase.__init__(self, endpoint, logger)
        self.providers = CloudformsProviders(endpoint, logger)
        self.tasks = CloudformsTasks(endpoint, logger)
        self.vms = CloudformsVMS(endpoint, logger)
