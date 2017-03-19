'''Module setup'''
from setuptools import setup


setup(
    name='Cloudforms',
    version='0.1.1',
    install_requires=[
        "requests"
    ],
    description='Cloudforms (ManageIQ) RESTful API Client',
    url='http://github.com/01000101',
    author='Joshua Cornutt',
    author_email='jcornutt@gmail.com',
    packages=['Cloudforms', 'Cloudforms.managers'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
