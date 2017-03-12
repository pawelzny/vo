import hashlib


class Value:
    """
    Basic implementation of DDD Value Object. These objects
    are meant to holds data only without any business logic.
    When data has no identifier so it is not an Entity,
    there comes Value Objects.
    
    Value Objects are consider same if they holds the same
    data even if allocated in different parts of memory.
    
    :Example:
    
    import vo
    
    value1 = vo.Value(name="test value", test=True)
    value2 = vo.Value(test=True, name="test value")
    assert(value1 == value2)  # True
    
    value1.set(extra="extra data")
    assert(value1 == value2)  # False
    """

    @staticmethod
    def to_bytes(string):
        """
        Converts string to byte string
        :param 
            string (str): String or number to convert
        :return
            (str): Byte string
        """

        return bytes(repr(string), 'utf-8')

    def __init__(self, **kwargs):
        """
        Dynamically add all kwargs to self dictionary.
        :param 
            kwargs: Key-value pairs 
        """

        self.set(**kwargs)

    def __eq__(self, other):
        """
        Predicate if checksum of Value Objects are the same.
        :param 
            other: ValueObject
        :return
            (bool): Boolean
        """

        return self.checksum() == other.checksum()

    def __ne__(self, other):
        """
        Predicate if checksum of Value Objects are different.
        :param 
            other: ValueObject
        :return
            (bool): Boolean 
        """

        return self.checksum() != other.checksum()

    def __hash__(self):
        """
        Returns hash of checksum
        :return 
            (int): Integer representing object Hash
        """

        return hash(self.checksum())

    def set(self, **kwargs):
        """
        Set additional attributes from kwargs
        :param 
            kwargs: 
        :return 
            (self): Returns self to allow method chaining.
        """

        self.__dict__.update(kwargs)

        return self

    def get(self, name, default=None):
        """
        Gets attribute value or default if not exists.
        :param 
            name (str): Attribute name
            default (any): Default value
        :return
            (any): Existing attribute value or default
        """

        return getattr(self, name, default)

    def checksum(self):
        """
        Computes and returns sha224 string from self dict items.
        :return
            (str): SHA224 string representing checksum of object values.
        """

        ck_sum = Value.to_bytes('checksum:')
        for key, value in sorted(self.__dict__.items()):
            ck_sum += Value.to_bytes(str(key) + str(value))

        return hashlib.sha224(ck_sum).hexdigest()
