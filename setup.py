#!/usr/bin/env python3
"""Define the setup options."""
import os
import re
import setuptools

with open('README.rst', 'r') as f:
    readme = f.read()


setuptools.setup(
    name='kaiterra-async-client',
    version='0.0.1',
    description="Kaiterra API Async Client",
    long_description=readme,
    long_description_content_type="text/x-rst",
    url='https://github.com/Michsior14/python-kaiterra-async-client',
    license='MIT License',
    packages=setuptools.find_packages(exclude=['tests']),
    test_suite='kaiterra_async_client.tests',
    tests_require=[
        'aioresponses',
        'aiounittest'
    ],
    install_requires=[
        'aiohttp>=3.6.0',
    ],
    # Uses enums (3.4) and type hints (3.5), though reducing this to >=3.5
    # by importing the typing package is a possibility
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
