#!/usr/bin/env python

from setuptools import setup

setup(
    name='tap-appsflyer',
    version='0.0.1',
    description='Singer.io tap for extracting data from the AppsFlyer API',
    author='ezCater, Inc.',
    url='http://singer.io',
    classifiers=['Programming Language :: Python :: 3 :: Only'],
    py_modules=['tap_appsflyer'],
    install_requires=[
        'attrs==16.3.0',
        'singer-python==1.6.0a2',
        'requests==2.12.4',
        'backoff==1.11.1',
    ],
    extras_require={
        'dev': [
            'bottle',
            'faker'
        ]
    },
    entry_points={
        'console_scripts': [
            'tap-appsflyer=tap_appsflyer:main'
        ]
    },
    packages=['tap_appsflyer'],
    package_data={
        'tap_appsflyer/schemas/raw_data': [
            'installations.json',
            'in_app_events.json'
        ],
    },
    include_package_data=True,
)
