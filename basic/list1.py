#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# © 2016 Lev Maximov

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    count=0
    for i in range(len(words)):
        stroka=words[i]
        if len(stroka)>=2 and stroka[0]==stroka[len(stroka)-1]:
            count+=1
    return count

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    l1=[]
    l2=[]
    for i in range(len(words)):
        stroka=words[i]
        if stroka[0]=='x':
            l1.append(stroka)
        else:
            l2.append(stroka)
    l1.sort()
    l2.sort()
    return l1+l2
# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
# PS исходный список должен остаться неизменным (аналогично тому, как делает sorted)
def sortByLast(inputStr):
    return inputStr[len(inputStr)-1]

def sort_last(tuples):
    l1 = tuples[:]
    l1.sort(key=sortByLast)
    return l1

# D. stable_sort_last
# Сортировка в предыдущем задании нестабильна: порядок записей при совпадающем
# последнем элементе кортежа произволен. Надо стараться избегать таких сортировок.
# Отсортируйте их так, чтобы при совпадающем последнем элементе
# сортировка проводилась по предпоследнему, при совпадающих предпоследних -
# по предпредпоследнему и так далее.
def reverse(a_string):
    return a_string[::-1]

def sortBackOrder(inputStr):
    return inputStr[::-1]

def stable_sort_last(tuples):
    l1=tuples[:]
    return sorted(l1,key=sortBackOrder)

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(('%s got: %s expected: %s' % (prefix, repr(got), repr(expected))))

# Calls the above functions with interesting inputs.
def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)
    test(match_ends(['абв', 'арра', 'ок', '']), 1)
    test(match_ends(['中文', '中文中', '中文中文', '中']), 1)

    print()
    print('front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
             ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
             ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
             ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

             
    print()
    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
             [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
             [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2,)]),
             [(2,), (1, 3), (3, 4, 5), (1, 7)])

    print()
    print('stable_sort_last')
    test(stable_sort_last([(1, 3), (3, 2), (2, 1)]),
             [(2, 1), (3, 2), (1, 3)])
    test(stable_sort_last([(2, 1), (1, 2), (3, 1)]),
             [(2, 1), (3, 1), (1, 2)])
    test(stable_sort_last([(1, 7), (4, 5), (3, 4, 5), (2,)]),
             [(2,), (4, 5), (3, 4, 5), (1, 7)])
    test(stable_sort_last('a b 1a 2a 11a 21a'.split()),
             'a 1a 11a 21a 2a b'.split())
    test(stable_sort_last(['1cat', '2cat', '10cat', 'dog', 'a dog']),
             ['dog', 'a dog', '10cat', '1cat', '2cat'])


if __name__ == '__main__':
    main()
