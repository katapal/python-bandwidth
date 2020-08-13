#!/usr/bin/env python
from setuptools import setup, find_packages


def get_version():
    version = {}
    with open('bandwidth_old/version.py') as f:
        exec(f.read(), version)
    return version.get('__version__')

setup(
    name='bandwidth_sdk',
    version=get_version(),
    description='This client library is designed to support the Bandwidth '
                'API and the official Bandwidth SDK',
    author='bandwidth_old',
    author_email='openapi@bandwidth_old.com',
    maintainer='bandwidth_old',
    maintainer_email='dtolb@bandwidth_old.com',
    url='https://github.com/bandwidth/python-bandwidth',
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    long_description="Bandwidth Python API",
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=[
        'requests',
        'python-dateutil',
        'six',
        'lxml'
    ],
)
