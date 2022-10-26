#!/usr/bin/env python3
import pytest
from operator import itemgetter
from itertools import *

# Реализуйте функцию-генератор, которая принимала бы на вход
# итерабельный объект (то есть, от которого можно "взять"
# итератор с помощью iter(a): контейнер, генератор или итератор)
# и возвращала бы итератор по элементам входной последовательности
# где удалены повторяющиеся элементы, при этом удаляться должны только 
# идущие подряд элементы (аналогично uniq в linux), например:
# [5, 1, 1, 5, 5] -> [5, 1, 5]

def remove_adjacent(it):
    return map(next, map(itemgetter(1), groupby(it)))

def test1(): assert list(remove_adjacent('')) == []
def test2(): assert list(remove_adjacent([1])) == [1]
def test3(): assert list(remove_adjacent([None, None, []])) == [None, []]
def test4(): assert list(remove_adjacent([3, 3, 1, 1, 6, 7, 7])) == [3, 1, 6, 7]
def test5(): assert list(remove_adjacent([-1, -1, -1, None, None, (), '', '', [], [], []])) == \
                                          [-1, None, (), '', []]
def test6(): assert list(remove_adjacent('a...   caaaat!!!')) == list('a. cat!')
def test7(): assert list(remove_adjacent('уууууурррррааааааа')) == list('ура')

if __name__ == '__main__':
    pytest.main([__file__])

