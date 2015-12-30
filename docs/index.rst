.. Cloudforms API v2 Python Client documentation master file, created by
   sphinx-quickstart on Thu Dec 17 00:22:54 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Cloudforms API v2 Python Client's documentation!
========================================================

This is the documentation for the community-supported Red Hat Cloudforms (ManageIQ) API v2 Python client.

Contents:

.. toctree::
   :maxdepth: 3
   :glob:

   api/*


Examples
========

List all virtual servers for the account::

    from Cloudforms import (
        Client,
        VSManager
    )

    client = Client(
        username='admin',
        password='smartvm',
        host='127.0.0.1'
    )
    vs_mgr = VSManager(client)
    instances = vs_mgr.list_instances()
    for instance in instances:
        print 'Server #%s: %s (%s)' % (
            instance.get('id'),
            instance.get('name'),
            instance.get('raw_power_state')
        )


External Links
==============
.. toctree::

    Cloudforms API Documentation <https://access.redhat.com/documentation/en/red-hat-cloudforms/>
    Source on GitHub <https://github.com/01000101/python-cloudforms/>
