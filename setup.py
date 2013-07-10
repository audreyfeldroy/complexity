#!/usr/bin/env python

import os
import sys

import complexity

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='complexity',
    version=complexity.__version__,
    description='A refreshingly simple static site generator, for those who like to work in HTML.',
    long_description=open('README.rst').read() + '\n\n' +
                     open('HISTORY.rst').read(),
    author='Audrey Roy',
    author_email='audreyr@gmail.com',
    url='https://github.com/audreyr/complexity',
    packages=[
        'complexity',
    ],
    package_data={'': ['LICENSE'], 'complexity': ['*.pem']},
    package_dir={'complexity': 'complexity'},
    entry_points={
        'console_scripts': [
            'complexity = complexity.complexity:command_line_runner',
        ]
    },
    include_package_data=True,
    install_requires=[
        'jinja2',
    ],
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(
        # 'Development Status :: 5 - Production/Stable',
        "Environment :: Console",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        # 'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ),
    keywords='complexity static site generator HTML Jinja2 templates S3',
)
