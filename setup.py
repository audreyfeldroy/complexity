#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with open('README.rst') as f:
    readme = f.read()
    
with open('HISTORY.rst') as f:
    history = f.read()
history = history.replace(".. :changelog:", "")

requirements = [
    'jinja2>=2.4',
    'binaryornot>=0.1.1',
    'PyYAML>=3.10'
]
test_requirements = []

if sys.version_info[:2] < (2, 7):
    requirements.append('argparse')
    test_requirements.append('unittest2')

setup(
    name='complexity',
    version='0.9.1',
    description='A refreshingly simple static site generator, for those who like to work in HTML.',
    long_description=readme + '\n\n' + history,
    author='Audrey Roy',
    author_email='audreyr@gmail.com',
    url='https://github.com/audreyr/complexity',
    packages=[
        'complexity',
    ],
    package_dir={'complexity': 'complexity'},
    entry_points={
        'console_scripts': [
            'complexity = complexity.main:main',
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='complexity,static site generator,HTML,Jinja2,templates,S3',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        "Environment :: Console",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
