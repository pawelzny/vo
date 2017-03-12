============
Value Object
============

:Info: DDD Value Objects implementation.
:Author: Paweł Zadrożny <pawel.zny@gmail.com>

Installation
============

.. code:: bash

    pip install vo


**Package**: https://pypi.python.org/pypi/vo


Example
=======

.. code:: python

    from vo.Value import Value

    value1 = Value(test=True, some_text="I am some text string")
    value2 = Value(some_text="I am some text string", test=True)

    assert(value1 == value2)  # True

    value1.set("extra_attr", "whatever")

    assert(value1 == value2)  # False
    assert("whatever" == value1.get("extra_attr"))  # True
    assert("default value" == value2.get("extra_attr", "default value"))  # True
