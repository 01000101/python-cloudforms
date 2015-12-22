# python-cloudforms
Red Hat Cloudforms RESTful API client written in Python.

This should work for both Red Hat Cloudforms (CFME) and ManageIQ (MIQ) appliances.

## Documentation
http://cloudforms-api-python-client.readthedocs.org/en/latest/

## Testing
Testing is relatively straight-forward.  Set up your environment variables (host, username, and password at minimum) and run whichever modules you'd like to test against.

```bash
export CLOUDFORMS_HOST=127.0.0.1
export CLOUDFORMS_USERNAME=admin
export CLOUDFORMS_PASSWORD=smartvm

pip install -r requirements.txt
python -u -m tests.main
```
