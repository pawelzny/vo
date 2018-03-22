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

* Value Objects are immutable.
* Two objects with the same values are considered equal
* Access to values with dot notation: ``value.my_attr``
* Access to values by key: ``value['my_attr']``


Installation
============

.. code:: bash

    pipenv install vo  # or pip install vo


**Package**: https://pypi.org/project/vo/


Documentation
=============

* Full documentation: http://vo.readthedocs.io
* Public API: http://vo.readthedocs.io/en/latest/api.html
* Examples and usage ideas: http://vo.readthedocs.io/en/latest/examples.html


Quick Example
=============

Value accept any ``key=value`` pairs. These pairs will be attached to object as attributes.
Once created values are immutable. Attributes can't be changed or deleted.

.. code-block:: python

   >>> from vo import Value
   >>> book = Value(title='Learning Python',
   ...              authors=['Mark Lutz', 'David Ascher'],
   ...              publisher="O'REILLY")
   >>> book
   Value(authors=['Mark Lutz', 'David Ascher'], publisher="O'REILLY", title='Learning Python')

   >>> str(book)
   '{"authors": ["Mark Lutz", "David Ascher"], "publisher": "O\'REILLY", "title": "Learning Python"}'


.. warning:: Any attempt of value modification or delete will raise ``ImmutableInstanceError``

.. code-block:: python

   >>> from vo import Value
   >>> book = Value(title='Learning Python',
   ...              authors=['Mark Lutz', 'David Ascher'],
   ...              publisher="O'REILLY")
   >>> book.title = 'Spam'
   Traceback (most recent call last):
     File "<input>", line 1, in <module>
       raise ImmutableInstanceError()
     vo.value.ImmutableInstanceError: Modification of Value frozen instance is forbidden.


Values access
-------------

Values can be accessed like object attributes or like dict keys.

.. code-block:: python

   >>> from vo import Value
   >>> book = Value(title='Learning Python',
   ...              authors=['Mark Lutz', 'David Ascher'],
   ...              publisher="O'REILLY")
   >>> book.title == book['title']
   True

   >>> book.authors == book['authors']
   True


Objects comparison
------------------

Let's take the same book example.

.. code-block:: python

   >>> from vo import Value
   >>> book1 = Value(title='Learning Python',
   ...               authors=['Mark Lutz', 'David Ascher'],
   ...               publisher="O'REILLY")
   >>> book2 = Value(title='Learning Python',
   ...               authors=['Mark Lutz', 'David Ascher'],
   ...               publisher="O'REILLY")
   >>> book1 == book2
   True

   >>> book1 is book2
   False


Value lookup
------------

Check if value exists.

.. code-block:: python

   >>> from vo import Value
   >>> book = Value(title='Learning Python',
   ...              authors=['Mark Lutz', 'David Ascher'],
   ...              publisher="O'REILLY")
   >>> 'title' in book
   True

   >>> 'price' in book
   False

   >>> book.title
   'Learning Python'

   >>> book.price
   Traceback (most recent call last):
     File "<input>", line 1, in <module>
   AttributeError: 'Value' object has no attribute 'price'
