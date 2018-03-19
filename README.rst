************
Value Object
************

:Info: DDD Value Object implementation.
:Author: Paweł Zadrożny @pawelzny <pawel.zny@gmail.com>

.. image:: https://circleci.com/gh/pawelzny/vo/tree/master.svg?style=shield&circle-token=bcc877f72e384d82ddd044b88de1faca2ff774bc
   :target: https://circleci.com/gh/pawelzny/vo/tree/master
   :alt: CI Status

.. image:: https://readthedocs.org/projects/vo/badge/?version=latest
   :target: http://vo.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/vo.svg
   :target: https://pypi.org/project/vo/
   :alt: PyPI Repository Status

.. image:: https://img.shields.io/github/release/pawelzny/vo.svg
   :target: https://github.com/pawelzny/vo
   :alt: Release Status

.. image:: https://img.shields.io/pypi/status/vo.svg
   :target: https://pypi.org/project/vo/
   :alt: Project Status

.. image:: https://img.shields.io/pypi/pyversions/vo.svg
   :target: https://pypi.org/project/vo/
   :alt: Supported python versions

.. image:: https://img.shields.io/pypi/implementation/vo.svg
   :target: https://pypi.org/project/vo/
   :alt: Supported interpreters

.. image:: https://img.shields.io/pypi/l/vo.svg
   :target: https://github.com/pawelzny/vo/blob/master/LICENSE
   :alt: License

Features
========

* Value object can't be changed once created
* Two objects with the same values are considered equal
* Access to values after dot: value.my_value
* Access to values like dict: value['my_value']


Installation
============

.. code:: bash

    pip install vo


**Package**: https://pypi.org/project/vo/


Documentation
=============

Read full documentation on: http://vo.readthedocs.io


Quick Example
=============

.. code:: python

   >>> from vo import Value
   ...
   >>> class Book(Value):
   ...     price = None
   ...     title = None
   ...     publisher = None
   ...
   >>> book = Book(price=120, title='Python for masses', publisher='SPAM')
   >>> book
   Book(price=120, title='Python for masses', publisher='SPAM')

   >>> book.title
   'Python for masses'

   >>> book['price']
   120

   >>> book.price = 230
   Traceback (most recent call last):
     File "<input>", line 1, in <module>
       raise ImmutableInstanceError
   vo.value.ImmutableInstanceError: Modification of Value instance is forbidden.
