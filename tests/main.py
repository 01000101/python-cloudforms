'''Red Hat Cloudforms REST API interface'''
import logging
from os import environ
import unittest
import Cloudforms

# Set our logging format
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s [%(funcName)s():%(lineno)d] %(message)s'
)

CLOUDFORMS_HOST = environ.get('CLOUDFORMS_HOST')
CLOUDFORMS_USERNAME = environ.get('CLOUDFORMS_USERNAME')
CLOUDFORMS_PASSWORD = environ.get('CLOUDFORMS_PASSWORD')
AWS_REGION = environ.get('AWS_REGION')
AWS_ACCESS_KEY = environ.get('AWS_ACCESS_KEY')
AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
AWS_NAME = 'PythonCF_Test'
AWS_PROVIDER = 'EmsAmazon'


def get_client():
    '''Gets a sugared connection to the client'''
    return Cloudforms.Client(
        host=CLOUDFORMS_HOST,
        username=CLOUDFORMS_USERNAME,
        password=CLOUDFORMS_PASSWORD,
        logger=logging)


class TestInputs(unittest.TestCase):
    '''Generic tests'''
    def test_env(self):
        '''Tests environment variables'''
        self.assertTrue(CLOUDFORMS_HOST)
        self.assertTrue(CLOUDFORMS_USERNAME)
        self.assertTrue(CLOUDFORMS_PASSWORD)


class TestVSManager(unittest.TestCase):
    '''Tests VSManager'''
    def test_list(self):
        '''Tests VSManager.list_instances()'''
        client = get_client()
        vs_mgr = Cloudforms.VSManager(client)
        # Test without params
        res = vs_mgr.list_instances()
        self.assertTrue(isinstance(res, list))
        # Test with params
        res = vs_mgr.list_instances({'attributes': 'id,name'})
        self.assertTrue(isinstance(res, list))

if __name__ == '__main__':
    unittest.main()
