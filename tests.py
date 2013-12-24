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
    assert not d.has_key(2)