#!/usr/bin/env python3
import pytest
from math import inf

# Напишите класс p_iter, который реализовывал бы
# обычной протокол итератора, но помимо этого
# позволял бы «подсмотреть» следующий элемент:
# >>> a = PeakableIterator('house')	
# >>> a.peek
# 'h'
# >>> list(a)
# ['h', 'o', 'u', 's', 'e']

# При помощи этого итератора напишите функцию,
# которая принимала бы на вход два итерабельных объекта
# представляющие собой отсортированные последовательности
# и проводила бы «слияние» двух итераторов в один 
# с сохранением отсортированного порядка
def compare(a,b):
	return (a>b)-(a<b)

class p_iter:
    def __init__(self, i):
        self._it = iter(i)
        self._next_el = None
        self._ifnext = 0
        self._check()


    def get_ifnext(self):
        return self._ifnext


    def peek(self):
        if self.get_ifnext():
        	return self._next_el


    def __next__(self):
        if not self._ifnext:
            raise StopIteration
        result = self._next_el
        self._check()
        return result


    def _check(self):
        try:
            self._next_el = next(self._it)
            self._ifnext = 1
        except StopIteration:
            self.next_el = None
            self._ifnext = 0

def merge(a, b):
    left, right = p_iter(a), p_iter(b)
    while True:
        if not left.get_ifnext():
            while 1: yield next(right)
        if not right.get_ifnext():
            while 1: yield next(left)
        comparison = compare(left.peek(), right.peek())
        if comparison < 0:
            yield next(left)
        elif comparison == 0:
            right.next() ; yield next(left)
        else:
            yield next(right)

def test1():  assert list(merge([], [])) == []
def test2():  assert list(merge([1], [])) == [1]
def test3():  assert list(merge([], [1])) == [1]
def test4():  assert list(merge([1, 8, 9], [2, 5, 6])) == [1, 2, 5, 6, 8, 9]
def test5():  assert list(merge([1, 8], [2, 5, 6])) == [1, 2, 5, 6, 8]
def test6():  assert list(merge([1, 8, 9], [2, 5])) == [1, 2, 5, 8, 9]
def test7():  assert list(merge([-2, 0, inf], [-1, 8])) == [-2, -1, 0, 8, inf]
def test8():  assert list(merge('az', 'def')) == list('adefz')
def test9():  assert list(merge('aez', 'df')) == list('adefz')
def test10(): assert list(merge(( (), ((),(),()) ), 
                                ( ((),()),  ((),)*5 ) )) == \
                                [ (), ((),()), ((),(),()), ((),)*5 ]

if __name__ == '__main__':
    pytest.main([__file__])

