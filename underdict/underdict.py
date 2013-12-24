class D(object):
    def __init__(self, items):
        self._items = items

    def __str__(self):
        return 'D{' + ', '.join('%s:%s' % i for i in self._items) + '}'

    def __repr__(self):
        return 'D([' + ', '.join('(%s, %s)' % i for i in self._items) + '])'

    def __getitem__(self, k):
        val = self.get(k)
        if val is None:
            raise KeyError(str(k))
        return val

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        return all([(s == o) for s, o in zip(self._items, other.items())])

    def keys(self):
        return [k for k, v in self._items]

    def values(self):
        return [v for k, v in self._items]

    def items(self):
        return [(k, v) for k, v in self._items]

    def has_key(self, k):
        return k in self.keys()

    def has_value(self, v):
        return v in self.values()

    def has_item(self, item):
        return item in self._items

    def get(self, k, default=None):
        for _k, v in self._items:
            if _k == k:
                return v
        else:
            return default


    def append(self, k, v):
        items = self._items + [(k, v)]
        return D(items)

    def prepend(self, k, v):
        items = [(k, v)] + self._items
        return D(items)

    def insert(self, index, k, v):
        items = self._items[:index] + [(k, v)] + self._items[index:]
        return D(items)


    def transpose(self):
        return D([(v, k) for k, v in self._items])


    def sort(self, cmp=None, key=None, reverse=False):
        return D(sorted(self._items, cmp, key, reverse))

    def reverse(self):
        return self.sort(key=lambda item: item[0], reverse=True)

    def key_sort(self, reverse=False):
        return self.sort(key=lambda item: item[0], reverse=reverse)

    def value_sort(self, reverse=False):
        return self.sort(key=lambda item: item[1], reverse=reverse)


    def map(self, fxn):
        """
        Returns a new underdict, which is the map of the given function over the
        items in the underdict. The function will be passed each key and value,
        and must return the new key and value in a a 2-tuple.
        """
        return D([fxn(k, v) for k, v in self._items])

    def map_values(self, fxn):
        """
        Returns a new underdict, which is the map of the given function over the
        values of the underdict. The function will be passed each key and value,
        and must return a single value.

        This is just a special case of D.map().
        """
        return self.map(lambda k, v: (k, fxn(k, v)))

    def map_keys(self, fxn):
        """
        Returns a new underdict, which is the map of the given function over the
        keys of the underdict. The function will be passed each key and value,
        and must return a single value.

        This is just a special case of D.map().
        """
        return self.map(lambda k, v: (fxn(k, v), v))

    def filter(self, fxn):
        """
        Returns an underdict containing the items for which the passed function
        returns True. The function is passed each key and value.
        """
        return D([(k, v) for k, v in self._items if fxn(k, v)])

    def reduce(self, fxn, initial):
        """
        Applies a 3-argument function successively to the keys and values of the
        underdict ie it computes fxn(...fxn(fxn(initial, k1, v1), k2, v2)...kn, vn)
        """
        val = initial
        for k, v in self._items:
            val = fxn(val, k, v)
        return val
