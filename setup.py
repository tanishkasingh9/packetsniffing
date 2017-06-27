# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='packagesniff',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Tanishka Singh',
    author_email='tanishka996@gmail.com',
    url='https://github.com/tanishkasingh9/packetsniffing',
    license=license,
    packages=find_packages(exclude=('tests'))
)

