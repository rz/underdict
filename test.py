from underdict import _D

def test_equals():
    l1, l2 = [(i, 2*i) for i in range(10)], [(i, 2*i) for i in range(10)]
    d1, d2 = _D(l1), _D(l2)
    assert d1 == d2, "_Ds should be equal but are not."

    l2[3] = (5, 6)
    assert not d1 == d2, "_Ds are equal but shoudln't be"
    assert d1 != d2, "_Ds are equal but shoudln't be"

def test_len():
    for i in range(5):
        d = _D([(x, x) for x in range(i)])
        assert len(d) == i


def test_get_item():
    d = _D([(1, 10), (2, 20)])
    assert d[1] == 10
    assert d[2] == 20
    try:
        d[3]
    except KeyError:
        assert True
    else:
        assert False, "Expected KeyError"