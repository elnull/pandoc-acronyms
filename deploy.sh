#!/bin/sh
# See .gitlab-ci.yml for the expected variables that configure twine:
echo "Packaging version $PACKAGE_VERSION for deployment..."
python3 setup.py sdist bdist_wheel
REPOSITORY="${TWINE_REPOSITORY_URL:-https://pypi.org}"
echo "Deploying to pypi repository $REPOSITORY..."
export TWINE_NON_INTERACTIVE=1
python3 -m twine upload --username __token__ dist/*
