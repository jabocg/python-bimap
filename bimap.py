"""Bidirectional Map in Python."""


class Bimap():
    """Store key-value pairs in a one-to-one mapping.

    Values can be retrieved by keys and keys can be retrieved by
    values(bidirectional).
    """

    def __init__(self, values=None):
        """Initialize a Bimap.

        Values is a dictionary with the initial values.
        """
        self._key_value_dict = {}
        self._value_key_dict = {}
        if values is not None:
            if not isinstance(values, dict):
                raise ValueError('values is not a dictionary')
            self._key_value_dict = values
            for k, v in values.items():
                self._value_key_dict[v] = k

    def __len__(self):
        """Return the length of the bimap."""
        return len(self._key_value_dict)

    def __contains__(self, value):
        """Return True if the bimap contains the value."""
        return value in self._key_value_dict or value in self._value_key_dict

    def __getitem__(self, key):
        """Return the associated value for the given key."""
        if key in self._key_value_dict:
            return self._key_value_dict[key]
        if key in self._value_key_dict:
            return self._value_key_dict[key]
        raise KeyError(key)

    def __setitem__(self, key, value):
        """Associate the given key with the given value."""
        if key in self._key_value_dict or key in self._value_key_dict:
            raise KeyError('Association for "{}" already exists'
                           .format(key))
        if value in self._key_value_dict or key in self._value_key_dict:
            raise KeyError('Association for "{}" already exists'
                           .format(value))
        self._key_value_dict[key] = value
        self._value_key_dict[value] = key

    def __delitem__(self, key):
        """Remove an association from the bimap."""
        if key not in self._key_value_dict and key not in self._value_key_dict:
            raise KeyError(key)
        if key in self._key_value_dict:
            value = self._key_value_dict[key]
            del self._key_value_dict[key]
            del self._value_key_dict[value]
        elif key in self._value_key_dict:
            value = self._value_key_dict[key]
            del self._value_key_dict[key]
            del self._key_value_dict[value]

    def __iter__(self):
        """Set up for bimap iteration."""
        self._keys = list(self._key_value_dict.keys())
        self._key_index = 0
        return self

    def __next__(self):
        """Return the next association."""
        if self._key_index >= len(self._key_value_dict):
            raise StopIteration
        key = self._keys[self._key_index]
        value = self._key_value_dict[key]
        self._key_index += 1
        return (key, value)

    def __str__(self):
        """Return a pretty string representation of the bimap."""
        str_list = []
        for k, v in self._key_value_dict.items():
            str_list.append('{} <-> {}'.format(repr(k), repr(v)))
        return '{{{}}}'.format(', '.join(str_list))

    def __repr__(self):
        """Return a constructable version of the bimap."""
        str_list = []
        for k, v in self._key_value_dict.items():
            str_list.append('{}: {}'.format(repr(k), repr(v)))
        return '{{{}}}'.format(', '.join(str_list))

    def __eq__(self, other):
        """Return True if two bimaps are equal.

        If they are not equal, or are different types, return False.
        """
        if not isinstance(other, Bimap):
            return False
        for a in other:
            if a[0] not in self or a[1] not in self:
                return False
        return True
