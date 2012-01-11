#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from distutils.core import setup

setup(
    name='django-geoip-utils',
    version='0.0.4',
    description='GeoIp data as an app to facilitate installing. Also features template filters, util functions and management commands for updating the data.',
    long_description=open('README.rst').read(),
    author='Philipp Wassibauer',
    author_email='phil@gidsy.com',
    url='http://github.com/Gidsy/django-geoip-utils',
    packages=[
        'geoip_utils',
        'geoip_utils.management',
        'geoip_utils.management.commands',
        'geoip_utils.templatetags',
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