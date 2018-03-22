#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Paweł Zadrożny'
__copyright__ = 'Copyright (c) 2017, Pawelzny'


# noinspection PyUnusedLocal
def vo_inheritance():
    from vo import Value

    class Book(Value):
        title = None
        author = None
        price = None
        currency = None

    book = Book(title='DDD', author='Pythonista', price=120.44, currency='USD')
    return


def vo_inheritance_wonky():
    from vo import Value

    class Book(Value):
        title = None
        author = None
        price = None
        currency = None

    book = Book(spam='Foo')

    # whaaaat!?

    assert 'spam' in book
    assert book.title is None
    assert book.price is None
    assert book.title is None
    assert book.currency is None
    return


# noinspection PyUnusedLocal
def proper_inheritance():
    from vo import Value

    class Book(Value):
        title = None
        author = None
        price = None
        currency = None

        def __init__(self, title, author, price, currency):
            # make validation if needed

            # always delegate assignment to Parent!
            super().__init__(title=title, author=author, price=price, currency=currency)

    book = Book(title='DDD', author='Pythonista', price=120.44, currency='USD')
    return


# noinspection PyUnusedLocal,PyMethodMayBeStatic
class Requests:
    """Fake request package for example purpose.
    Original package can be found at http://docs.python-requests.org/en/master/

    Example response comes from https://quotesondesign.com/
    """

    def get(self, url):
        return self

    def json(self):
        return [
            {
                "ID": 2423,
                "title": "John Maeda",
                "content": "<p>Design is a solution to a problem. "
                           "Art is a question to a problem.</p>\n",
                "link": "https://quotesondesign.com/john-maeda-5/"
            },
            {
                "ID": 2379,
                "title": "Ricardo Zea",
                "content": "<p>Learning Web Design is like playing video games: "
                           "You start small and build your character as you "
                           "progress, then you beat the boss, literally.</p>\n",
                "link": "https://quotesondesign.com/ricardo-zea/"
            }
        ]


requests = Requests()


# noinspection PyUnusedLocal
def idea_frozen_response():
    from vo import Value

    class Quote(Value):
        ID = None
        title = None
        content = None
        link = None

        def __init__(self, ID, title, content, link, **kwargs):
            # validation if needed
            super().__init__(ID=ID, title=title, contet=content, link=link)

    response = requests.get('https://quotesondesign.com/wp-json/posts'
                            '?filter[orderby]=rand'
                            '&filter[posts_per_page]=2')

    quotes = [Quote(**item) for item in response.json()]
    return


def idea_coordinates():
    from vo import Value

    class Point2D(Value):
        x = 0
        y = 0

        def __init__(self, x, y):
            if not isinstance(x, (int, float)):
                raise TypeError('x must be a number')
            if not isinstance(y, (int, float)):
                raise TypeError('y must be a number')

            super().__init__(x=x, y=y)

        def __add__(self, other):
            return Point2D(self.x + other.x, self.y + other.y)

        def __sub__(self, other):
            return Point2D(self.x - other.x, self.y - other.y)

    p1 = Point2D(2, 5)
    p2 = Point2D(2, 5)
    p3 = Point2D(-3, 10)

    assert p1 == p2
    assert p1 != p3
    assert p1 + p2 == Point2D(4, 10)
    assert p3 - p1 == Point2D(-5, 5)
    # end of coordinates


def idea_money():
    import decimal
    from vo import Value

    class Money(Value):
        amount = None

        def __init__(self, amount=0.00):
            super().__init__(amount=decimal.Decimal(amount))

        def __lt__(self, other):
            return self.amount < other.amount

        def __gt__(self, other):
            return self.amount > other.amount

        def __eq__(self, other):
            return self.amount == other.amount

        def __add__(self, other):
            return Money(amount=self.amount + other.amount)

        def __sub__(self, other):
            return Money(amount=self.amount - other.amount)

    assert Money(200) > Money(120)
    assert Money(100) < Money(120)
    assert Money(100) + Money(200) == Money(300)
    assert Money(100) - Money(50) == Money(50)
    # end of money
