import pytest
from itertools import *
import operator
import collections
from collections import deque

# Все функции должны возвращать итератор.

# Можно использовать как генератор-функции (то есть через yield) и 
# генератор-выражения (list-comprehension с круглыми скобками),
# так и helper'ы из itertools, builtins и пр.

def tail(iterable, n):
    "Return an iterator over the last n items, лучше всего через deque"
    "с ограниченной длиной"
    return iter(deque(iterable, maxlen=n))

def pairs(iterable):
    """ Сгруппируйте элементы итерабельного объекта попарно:
    (1, 2, 3, 4, 5, 6) -> [(1, 2), (3, 4), (5, 6)]
    Если длина нечетная, последний элемент можно игнорировать
    На входе - итерабельный объект, на выходе - итератор

    """
    it = iter(iterable)
    itnext=next(it)
    itnext2=next(it)
    print(itnext, itnext2)
    while True:
        try:
            yield (itnext,itnext2)
            itnext=next(it)
            itnext2=next(it)
        except:
            break

def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    seen = set() #создал множество неповторяющихся элементов
    if key is None:
        for element in filterfalse(seen.__contains__, iterable): 
            seen.add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen.add(k)
                yield element

def iter_except(f, exception, first=None):
    """ Вызывает функцию f до тех пор, пока та не сгенерирует исключение exception.

    Превращает интерфейс «call-until-exception» в интерфейс итератора.
    Аналогично builtins.iter(func, sentinel) но использует исключение вместо
    sentinel в качестве условия выхода из цикла 
    
    Если задан отличный от None аргумент first, возвращает его перед первым запуском
    функции.

    Возвращает итератор.

    """
    try:
        if first is not None:
            yield first()   
        while True:
            yield f()
    except exception:
        pass

def map_longest(f, *iterables, fillvalue=None):
    """ Расширенная версия функции map (аналогичная zip_longest), которая,
    когда один или несколько входных итераторов исчерпаются, использовала бы 
    значение fillvalue вполть до последнего элемента самого длинного итератора.
    """
    # Здесь может пригодиться форма вызова функции через tuple,
    # например: a = ('input.txt, 'rb'); open(*a)
    return map(f,*zip(*zip_longest(*iterables, fillvalue=fillvalue)))


def test1():
    assert ''.join(tail('ABCDEFG', 3)) == 'EFG'

def test2():
    def to_be():
        for i in 'tobeornottobe':
            yield i
    assert list(pairs([])) == []
    assert list(pairs([1, 2])) == [(1, 2)]
    assert list(pairs([1, 2, 3])) == [(1, 2)]
    assert list(pairs([1, 2, 3, 4, 5, 6])) == [(1, 2), (3, 4), (5, 6)]
    assert list(pairs('abcdefg')) == [('a', 'b'), ('c', 'd'), ('e', 'f')]
    assert list(pairs(to_be())) == [('t', 'o'), ('b', 'e'), ('o', 'r'),
                                    ('n', 'o'), ('t', 't'), ('o', 'b')]

def test3():
    assert ''.join(unique_everseen('AAAABBBCCDAABBB')) == 'ABCD'
    assert ''.join(unique_everseen('ABBcCAD', str.lower)) == 'ABcD'

def test4():
    d = collections.deque(('some', 'like', 'it', 'hot'))
    assert list(iter_except(d.pop, IndexError)) == ['hot', 'it', 'like', 'some']

def test5():
    assert list(map_longest(lambda a,b: a+b, (2,3), (3,5))) == [5, 8]
    assert list(map_longest(lambda a,b: a+b, (2, 3), (3, 4, 5), fillvalue=1)) == [5, 7, 6]
    assert list(map_longest(lambda a,b: a+b, (2, 3, 1), (3, 4), fillvalue=5)) == [5, 7, 6]


if __name__ == '__main__':
    # При таком способе вызова каждый assert вместо просто да/нет будет
    # выдавать более детальную информацию, если что-то пошло не так.
    pytest.main([__file__])
#    pytest.main(['__file__ + '::test3'])    # запускает только третий тест
#    pytest.main(['-s', __file__ + '::test3'])   # то же + возможность отладки ipdb
