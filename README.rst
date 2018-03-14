============
Value Object
============

:Info: DDD Value Objects implementation.
:Author: Paweł Zadrożny @pawelzny <pawel.zny@gmail.com>


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


**Package**: https://pypi.python.org/pypi/vo


Example
=======

.. code:: python

    from vo import Value

    value1 = Value(test=True, some_text="I am some text string")
    value2 = Value(some_text="I am some text string", test=True)
    value3 = Value(purpose_of_life=42)

    assert(value1 == value1)  # True
    assert(value1 == value2)  # True
    assert(value1 == value3)  # False

    print(value3.purpose_of_life)  # 42
    print(value3['purpose_of_life'])  # 42
