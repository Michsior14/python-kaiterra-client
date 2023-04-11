#!/usr/bin/env python3
"""Define the setup options."""
import os
import re
import setuptools

with open('README.rst', 'r') as f:
    readme = f.read()


setuptools.setup(
    name='kaiterra-async-client',
    version='1.0.1',
    description="Kaiterra API Async Client",
    long_description=readme,
    long_description_content_type="text/x-rst",
    url='https://github.com/Michsior14/python-kaiterra-async-client',
    license='MIT License',
    packages=setuptools.find_packages(exclude=['*.tests', '*.tests.*']),
    test_suite='kaiterra_async_client.tests',
    tests_require=[
        'aioresponses',
        'aiounittest'
    ],
    install_requires=[
        'aiohttp>=3.8.1',
    ],
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
