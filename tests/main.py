'''Red Hat Cloudforms REST API interface'''
import logging
from os import environ
from distutils.version import StrictVersion
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


class TestVersion(unittest.TestCase):
    '''API version tests'''
    def test_version(self):
        '''Tests API version information'''
        client = get_client()
        data = client.call('get', '/')
        self.assertEqual(data.get('name'), 'API')
        self.assertEqual(data.get('description'), 'REST API')
        self.assertTrue(
            StrictVersion(data.get('version')) > StrictVersion('2.0'))


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
        logging.info('res: %s [%s]', res, type(res))
        self.assertTrue(isinstance(res, list))
        # Test with params
        res = vs_mgr.list_instances({'attributes': 'id,name'})
        logging.info('res: %s [%s]', res, type(res))
        self.assertTrue(isinstance(res, list))


class TestProviderManager(unittest.TestCase):
    '''Tests ProviderManager'''
    def test_create(self):
        '''Tests ProviderManager.create_amazon_provider()'''
        client = get_client()
        prov_mgr = Cloudforms.ProviderManager(client)
        logging.info('Creating Amazon provider')
        prov = prov_mgr.create_amazon_provider(
            AWS_NAME,
            'us-east-1',
            AWS_ACCESS_KEY,
            AWS_SECRET_KEY)
        logging.info('Result: %s', prov)
        self.assertNotEqual(prov.get('id'), None)

    def test_refresh(self):
        '''Tests ProviderManager.refresh_provider()'''
        client = get_client()
        prov_mgr = Cloudforms.ProviderManager(client)
        provs = prov_mgr.list_providers()
        for prov in provs:
            if prov.get('name') == AWS_NAME:
                self.assertNotEqual(prov.get('id'), None)
                prov_mgr.refresh_provider(prov.get('id'))

    def test_delete(self):
        '''Tests ProviderManager.delete_provider()'''
        client = get_client()
        prov_mgr = Cloudforms.ProviderManager(client)
        provs = prov_mgr.list_providers()
        for prov in provs:
            if prov.get('name') == AWS_NAME:
                self.assertNotEqual(prov.get('id'), None)
                prov_mgr.delete_provider(prov.get('id'))

if __name__ == '__main__':
    unittest.main()
