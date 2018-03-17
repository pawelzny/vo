==========
Public API
==========


*****************
Instance of Value
*****************

.. py:module:: vo.value
.. autoclass:: Value
   :member-order: bysource
   :members:


Create new instance of Value
============================

Value accept any key=value pairs. These pairs will be attached to object as attributes.
Once created values are immutable. Can't be changed or deleted.

.. code-block:: python

   >>> from vo import Value
   >>> book = Value(title='Learning Python',
   ...              authors=['Mark Lutz', 'David Ascher'],
   ...              publisher="O'REILLY")
   >>> book
   <vo.value.Value object at 0x7f38862b3860>


Values access
=============

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
==================

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
============

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


****************************
Modification forbidden error
****************************

.. py:module:: vo.value
.. autoexception:: ImmutableInstanceError
   :members:
   :undoc-members:


Any attempt of value modification or delete will raise `ImmutableInstanceError`

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
