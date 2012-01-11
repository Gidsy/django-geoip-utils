#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from distutils.core import setup

setup(
    name='django-geoip-utils',
    version='0.0.2',
    description='GeoIp data as an app to facilitate installing. Also features management commands for updating the data.',
    long_description=open('README.rst').read(),
    author='Philipp Wassibauer',
    author_email='phil@gidsy.com',
    url='http://github.com/Gidsy/django-geoip-data',
    packages=[
        'geoip_utils',
    ],
    package_data={'geoip_utils': [
		'data/*.dat'
	]},
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)