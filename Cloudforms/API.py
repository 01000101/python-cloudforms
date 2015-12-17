'''Cloudforms public library interface'''
from Cloudforms.utils import CloudformsBase, CloudformsEndpoint


# pylint: disable=too-few-public-methods
class Client(CloudformsBase):
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
