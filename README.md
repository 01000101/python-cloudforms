# python-cloudforms
Red Hat Cloudforms RESTful API v2 client written in Python.

This should work for both Red Hat Cloudforms 4.0+ (CFME 5.5.0+) and ManageIQ (MIQ) appliances.

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

Some tests will require more specific information to do testing (such as provider tests).  For example, if you'd like to test provider functions, you'll need to provide provider details (Amazon in this case).

Obviously, you'll need to replace these values with your own (in addition to the base variables above). Once you've got the variables in place, you can execute the tests individually if you'd like.

```bash
export AWS_REGION=us-east-1
export AWS_ACCESS_KEY=XXIAJJZZYYXXGD2MTLAA
export AWS_SECRET_KEY=8qxp1w/H194PEkEOhcENsvPHb5IQZK1rh8KX3xc6

python -u -m unittest tests.main.TestProviderManager
```
