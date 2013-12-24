from underdict import D


def test_equals():
    l1, l2 = [(i, 2*i) for i in range(10)], [(i, 2*i) for i in range(10)]
    d1, d2 = D(l1), D(l2)
    assert d1 == d2, "Ds should be equal but are not."

    l2[3] = (5, 6)
    assert not d1 == d2, "Ds are equal but shoudln't be"
    assert d1 != d2, "Ds are equal but shoudln't be"


def test_len():
    for i in range(5):
        d = D([(x, x) for x in range(i)])
        assert len(d) == i


def test_get_item():
    d = D([(1, 10), (2, 20)])
    assert d[1] == 10
    assert d[2] == 20
    try:
        d[3]
    except KeyError:
        pass
    else:
        assert False, "Expected KeyError"

def test_keys():
    keys = [i for i in range(10)]
    d = D([(k, 2*k) for k in keys])
    assert d.keys() == keys

def test_values():
    values = [i for i in range(10)]
    d = D([(v, v) for v in values])
    assert d.values() == values

def test_items():
    items = [(k, 2*k) for k in range(10)]
    d = D(items)
    assert d.items() == items

def test_has_key():
    d = D([(1, 10)])
    assert d.has_key(1)
    assert not d.has_key(10)
    assert not d.has_key(2)

def test_has_value():
    d = D([(1, 10)])
    assert d.has_value(10)
    assert not d.has_value(1)
    assert not d.has_value(20)

def test_has_item():
    d = D([(1, 10)])
    assert d.has_item((1, 10))
    assert not d.has_item((10, 1))
    assert not d.has_item((2, 10))

def test_get():
    d = D([(k, 2*k) for k in range(10)])
    assert d.get(1) == 2
    assert d.get(3) == 6
    assert d.get(20) is None
    assert d.get(20, 'default') == 'default'

def test_append():
    d = D([(2, 4), (3, 6)])
    d = d.append(4, 8)
    assert d.has_key(4)
    assert d.has_value(8)
    assert d == D([(2, 4), (3, 6), (4, 8)])

def test_prepend():
    d = D([(2, 4), (3, 6)])
    d = d.prepend(4, 8)
    assert d.has_key(4)
    assert d.has_value(8)
    assert d == D([(4, 8), (2, 4), (3, 6)])

def test_insert():
    d = D([(2, 4), (4, 8)])
    d = d.insert(1, 3, 6)
    assert d.has_key(3)
    assert d.has_value(6)
    assert d == D([(2, 4), (3, 6), (4, 8)])

def test_transpose():
    d = D([(k, 2*k) for k in range(10)]).transpose()
    assert d == D([(2*k, k) for k in range(10)])

def test_sort():
    d = D([(2, 4), (1, 2), (0, 10)])
    assert d.sort(key=lambda i: i[0]) == D([(0, 10), (1, 2), (2, 4)])
    assert d.sort(key=lambda i: i[1]) == D([(1, 2), (2, 4), (0, 10)])
    assert d.sort(key=lambda i: i[0], reverse=True) == D([(2, 4), (1, 2), (0, 10)])

def test_reverse():
    d = D([(0, 0), (1, 2), (2, 4)])
    assert d.reverse() == D([(2, 4), (1, 2), (0, 0)])

def test_key_sort():
    d = D([(2, 4), (1, 2), (0, 10)])
    assert d.key_sort() == D([(0, 10), (1, 2), (2, 4)])

def test_value_sort():
    d = D([(2, 4), (1, 2), (0, 10)])
    assert d.value_sort() == D([(1, 2), (2, 4), (0, 10)])

def test_map():
    d = D([(k, 2*k) for k in range(10)])
    assert d.map(lambda k, v: (2*k, 10*k)) == D([(2*k, 10*k) for k in range(10)])

def test_map_values():
    d = D([(k, 2*k) for k in range(10)])
    assert d.map_values(lambda k, v: k+v) == D([(k, 3*k) for k in range(10)])

def test_map_keys():
    d = D([(k, 2*k) for k in range(10)])
    assert d.map_keys(lambda k, v: k+v) == D([(3*k, 2*k) for k in range(10)])

def test_filter():
    d = D([(k, 2*k) for k in range(10)])
    assert d.filter(lambda k, v: k % 2 == 0) == D([(k, 2*k) for k in range(0, 10, 2)])

def test_reduce():
    d = D([(k, 2*k) for k in range(5)])
    key_sum = 0 + 1 + 2 + 3 + 4
    val_sum = 0 + 2 + 4 + 6 + 8
    assert d.reduce(lambda acc, k, v: acc + k, 0) ==  key_sum
    assert d.reduce(lambda acc, k, v: acc + v, 0) ==  val_sum
    assert d.reduce(lambda acc, k, v: acc + k + v, 0) == key_sum + val_sum
    assert d.reduce(lambda acc, k, v: acc + k + v, 2) == 2 + key_sum + val_sum

