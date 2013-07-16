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

readme = open('README.rst', 'rt').read()
history = open('HISTORY.rst', 'rt').read().replace(".. :changelog:", "")

setup(
    name='complexity',
    version=complexity.__version__,
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
            'complexity = complexity.complexity:command_line_runner',
        ]
    },
    include_package_data=True,
    install_requires=[
        'jinja2',
    ],
    license="BSD",
    zip_safe=False,
    keywords='complexity,static site generator,HTML,Jinja2,templates,S3',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        "Environment :: Console",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    test_suite='tests',
)
