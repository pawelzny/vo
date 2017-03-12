# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='vo',
      version='0.1.0',
      description='DDD Value Objects implementation',
      long_description=readme,
      keywords='value data object DDD',
      author='Pawel Zadrozny @pawelzny',
      author_email='pawel.zny@gmail.com',
      url='https://github.com/pawelzny/vo',
      license=license,
      test_suite='nose.collector',
      tests_require=['nose', 'coverage'],
      packages=find_packages(exclude=('tests', 'docs', 'bin')),
      zip_safe=False)
