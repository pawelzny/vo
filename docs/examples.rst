========
Examples
========

Yes, I know it's dangerous to follow code examples.
Usually examples aren't in sync with real source code.

But I found a solution ... I hope!

.. note:: | All examples are derived from real code hooked to Pytest.
          | Every change in source code enforce change in examples.
          | **Outdated examples == failed build**.
          |
          | You can check at https://github.com/pawelzny/vo/blob/master/tests/test_examples.py

.. seealso:: Look at :ref:`Public API` for more details.

******
Basics
******

Value objects can be used as is straight from library.
You still can extend them but for simple usage its not necessary.


Create Value Object
===================

Value takes all kwargs (key=value) and add them as object attribute.
Assigning values are made only once on ``__init__`` and after that
no values can be changed.

.. literalinclude:: ../example/basics.py
   :language: python
   :dedent: 4
   :start-after: create_plain_value_object
   :end-before: return


Access to attributes
====================

Properties can be accessed with dot or key notation.

.. literalinclude:: ../example/basics.py
   :language: python
   :dedent: 4
   :start-after: access_value_properties
   :end-before: return


Value Objects comparison
========================

.. note:: Two objects with the same values are
          considered **equal**, but **not the same**.


Compare different values
------------------------

.. literalinclude:: ../example/basics.py
   :language: python
   :dedent: 4
   :start-after: compare_different_value_objects
   :end-before: return


Compare similar values
----------------------

.. literalinclude:: ../example/basics.py
   :language: python
   :dedent: 4
   :emphasize-lines: 7
   :start-after: compare_similar_value_objects
   :end-before: return

********
Advanced
********

More real life example of Value Object usage.

Basic inheritance
=================

Using Value Object directly is easy, fast, and just works.
However due to dynamic attribute assignment on ``__init__`` your favourite
IDE / Editor can't generate hints.

This is when inheritance come handy.

.. literalinclude:: ../example/advanced.py
   :language: python
   :dedent: 4
   :start-after: vo_inheritance
   :end-before: return


Wonky behaviour
===============

Weird behaviour but completely correct.

.. warning:: Value Object does not validate given attributes.
             Validation is up to you.

.. literalinclude:: ../example/advanced.py
   :language: python
   :dedent: 4
   :start-after: vo_inheritance_wonky
   :end-before: return


Attribute validation
====================

Most of the time you will want to make inheritance like below,
but remember to not assign attribute by your own. Always delegate to
``super().__init__()``

.. literalinclude:: ../example/advanced.py
   :language: python
   :dedent: 4
   :emphasize-lines: 12-13
   :start-after: proper_inheritance
   :end-before: return


Usage Ideas
===========

Value Object is helpful always when source data must not be modified.

Frozen response
---------------

.. note:: **Requests** package has been faked for purpose of this example to avoid
          unnecessary and unrelated dependency.

          Before executing this example make sure you have **requests**
          installed in your environment with ``pip install requests``

.. literalinclude:: ../example/advanced.py
   :language: python
   :dedent: 4
   :start-after: idea_frozen_response
   :end-before: return


2D Coordinates
--------------

.. literalinclude:: ../example/advanced.py
   :language: python
   :dedent: 4
   :start-after: idea_coordinates
   :end-before: # end of coordinates


Money object
------------

.. danger:: | **This example is not meant to run on production !!**
            | It doesn't implement validation and many more comparison methods.
            |
            | But its nice to present general idea of Money Object.

.. literalinclude:: ../example/advanced.py
   :language: python
   :dedent: 4
   :start-after: idea_money
   :end-before: # end of money


*****************
Forbidden actions
*****************

.. warning:: All attempt to value modification
             ends up with ``ImmutableInstanceError`` exception.


Modification
============

Modification of existing attribute is forbidden.
Let's create a book, and then try to change its title.

.. literalinclude:: ../example/forbidden.py
   :language: python
   :dedent: 4
   :emphasize-lines: 7
   :start-after: property_modification_forbidden
   :end-before: return

Adding new attributes also raises exception.
Let's add publisher property to the book.

.. literalinclude:: ../example/forbidden.py
   :language: python
   :dedent: 4
   :emphasize-lines: 7
   :start-after: adding_new_property_forbidden
   :end-before: return

Deletion
========

Properties of value object can't be deleted no matter what!

.. literalinclude:: ../example/forbidden.py
   :language: python
   :dedent: 4
   :emphasize-lines: 7
   :start-after: property_deletion_forbidden
   :end-before: return


**********
Data dumps
**********

Convert value object to different data types.

To dict
=======

.. note:: Actually ``.to_dict()`` method returns ``collections.OrderedDict``.

.. literalinclude:: ../example/dumps.py
   :language: python
   :dedent: 4
   :emphasize-lines: 4
   :start-after: dump_to_dict
   :end-before: return


To bytes
========

.. literalinclude:: ../example/dumps.py
   :language: python
   :dedent: 4
   :emphasize-lines: 4
   :start-after: dump_to_bytes
   :end-before: return

To JSON
=======

.. literalinclude:: ../example/dumps.py
   :language: python
   :dedent: 4
   :emphasize-lines: 4
   :start-after: dump_to_json
   :end-before: return
