class _D(object):
    def __init__(self, items):
        self._items = items

    def __str__(self):
        return '_D({' + ', '.join('%s:%s' % i for i in self._items) + '})'

    def __repr__(self):
        return '_D([' + ', '.join('%s, %s' % i for i in self._items) + '])'

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

    def has_value(self, k):
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
        return _D(items)

    def prepend(self, k, v):
        items = [(k, v)] + self._items
        return _D(items)

    def insert(self, index, k, v):
        items = self._items[:index] + [(k, v)] + self._items[index:]
        return _D(items)


    def transpose(self):
        return _D([(v, k) for k, v in items])


    def sort(self, cmp=None, key=None, reverse=False):
        return _D(sorted(self._items, cmp, key, reverse))

    def reverse(self):
        return self.sort(key=lambda pair: pair[0], reverse=True)

    def key_sort(self, reverse=False):
        return self.sort(key=lambda pair: pair[0], reverse=reverse)

    def value_sort(self, reverse=False):
        return self.sort(key=lambda pair: pair[1], reverse=reverse)


    def map(self, fxn):
        return _D(map(fxn, self._items))

    def filter(self, fxn):
        return _D(filter(fxn, self._items)))

    def reduce(self, fxn, initial):
        return _D(reduce(fxn, items, initial)))
