#!/bin/sh
# See .gitlab-ci.yml for the expected variables that configure twine:
COMMIT_DATETIME=$(git show --no-patch --no-notes --pretty='%cd' --date=format:'%Y%m%d%H%M')
export PACKAGE_VERSION="$(git describe  --always --tags --abbrev=0 HEAD).$SUFFIX$COMMIT_DATETIME"
echo "Packaging version $PACKAGE_VERSION for deployment..."
python3 setup.py sdist bdist_wheel
REPOSITORY="${TWINE_REPOSITORY_URL:-https://pypi.org}"
echo "Deploying to pypi repository $REPOSITORY..."
export TWINE_NON_INTERACTIVE=1
python3 -m twine upload --username __token__ dist/*
