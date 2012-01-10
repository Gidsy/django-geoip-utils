#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from distutils.core import setup

setup(
    name='geoip_data',
    version='0.0.1',
    description='GeoIp data as an app to facilitate installing. Also features management commands for updating the data.',
    long_description=open('README.rst').read(),
    author='Philipp Wassibauer',
    author_email='phil@gidsy.com',
    url='http://github.com/Gidsy/django-geoip-data',
    packages=[
        'geoip_data',
    ],
    package_data={'geoip_data': [
		'geoip_data/static/geoip_data/*.csv'
		'geoip_data/static/geoip_data/*.dat'
	]},
    # data_files=[('certifi', ['certifi/cacert.pem'])],
    include_package_data=True,
    classifiers=(
        'Development Status :: 4 - Production/Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)