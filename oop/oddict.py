from collections import OrderedDict

class OrderedDefaultDict(OrderedDict):
    def __init__(self, default_factory=None, *args, **kwargs):
        OrderedDict.__init__(self, *args, **kwargs)
        self.default_factory = default_factory

    def __missing__(self, key):
        if self.default_factory!=None:
            self[key] = value = self.default_factory()
            return value
        else:
            raise KeyError(key)

    def __repr__(self):
        return 'OrderedDefaultDict(%s, %s' % (self.default_factory,
                                               (OrderedDict.__repr__(self)[19:]))

def test1():
    a = OrderedDefaultDict(int)
    a['a'] += 1
    a['b'] += 2
    a['c'] += 3
    assert list(a.keys()) == ['a', 'b', 'c']
    assert dict(a.items()) == {'a': 1, 'b': 2, 'c': 3}
    del a['b']
    a['b'] += 4
    assert list(a.keys()) == ['a', 'c', 'b']

def test2():
    a = OrderedDefaultDict(list)
    a['q'].append(10)
    assert a['q'] == [10]
    assert repr(a) == "OrderedDefaultDict(<class 'list'>, [('q', [10])])"

if __name__ == '__main__':
    import pytest
    pytest.main(['-s', __file__])
