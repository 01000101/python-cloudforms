# Contribution Guidelines

## Pull requests

Fork the repo, create a feature / fix branch, make your commits, squash your
commits to a reasonable amount (usually 1-2 max), and create a PR to master with
meaningful PR comments.

Library functionality is tested manually by repo admins but code syntax
is tested using the tools below.


## Styling

All code must be able to pass a `flake8` test on the plugin package.
Steps to check this are as follows:

```bash
  pip install flake8
  flake8 Cloudforms/
```

All code must be able to pass a `pylint` test on the plugin package. If there are
parts that are misdetections, please use the appropriate `#pylint: disable=XXXXX`
statements (sparingly).

```bash
  pip install pylint
  pylint Cloudforms/
```
