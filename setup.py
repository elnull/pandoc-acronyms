import setuptools
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pandoc-acronyms',
    version='0.2',
    author="Mirko Boehm",
    author_email="mirko@kde.org",
    description="A Python filter to manage acronyms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/mirkoboehm/pandoc-acronyms",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        pandoc-acronyms=filter.pandocacronyms:filter
    ''',
    python_requires='>=3.6',
)
