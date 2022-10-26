#!/usr/bin/env python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# Перевод, дополнения Максимов Л.В. © 2016

from math import inf    # бесконечность

# Дополнительные упражнения на списки

# Дан список произвольных элементов. Требуется построить список
# в котором удалены идущие подряд одинаковые элементы (аналогично
# uniq в linux), например
# [5, 1, 1, 5, 5] -> [5, 1, 5]
# Исходный список должен остаться неизменным.
def remove_adjacent(nums):
    n = []
    if len(nums)>=2:
        n.append(nums[0])
        for i in range(len(nums))[1::]:
            if nums[i]!=nums[i-1]:
                n.append(nums[i])
    else:
        if nums=='':    
            return []
        else:
            n=nums[:]
    return n



# Даны два отсортированных списка. Необходимо построить новый список,
# содержащий элементы исходных в отсортированном порядке за линейное время,
# то есть за один проход как по исходным спискам и так и по результирующему.
# Исходные списки должны остаться неизменными.
def linear_merge(list1, list2):
    n=[]
    flag=False
    i=0
    j=0
    while i<(len(list1)) and j<(len(list2)):
        if list1[i] < list2[j]:
            n.append(list1[i])
            i=i+1
        else:
            n.append(list2[j])
            j=j+1
    n.extend(list1[i:])
    n.extend(list2[j:])   
    return n


# Функция test() используется в main() для сравнения того, 
# что возвращает функция, с тем, что она должна возвращать.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Вызывает определенные выше функции с тестовыми параметрами.
def main():
    print('remove_adjacent')
    test(remove_adjacent(''), [])
    test(remove_adjacent([1]), [1])
    test(remove_adjacent([None, None, []]), [None, []])
    test(remove_adjacent([7, 3, 3, 1, 1, 6, 7, 7, 1]), [7, 3, 1, 6, 7, 1])
    test(remove_adjacent([-1, -1, -1, None, None, (), '', '', [], [], []]),
                         [-1, None, (), '', []])
    test(remove_adjacent('a...   caaaat!!!'), list('a. cat!'))
    test(remove_adjacent('уууууурррррааааааа'), list('ура'))

    print()
    print('linear_merge')
    test(linear_merge([], []), [])
    test(linear_merge([1], []), [1])
    test(linear_merge([], [1]), [1])
    test(linear_merge([1, 8, 9], [2, 5, 6]), [1, 2, 5, 6, 8, 9])
    test(linear_merge([1, 8], [2, 5, 6]), [1, 2, 5, 6, 8])
    test(linear_merge([1, 8, 9], [2, 5]), [1, 2, 5, 8, 9])
    test(linear_merge([-2, 0, inf], [-1, 8]), [-2, -1, 0, 8, inf])
    test(linear_merge(list('az'), list('def')), list('adefz'))
    test(linear_merge(list('aez'), list('df')), list('adefz'))
    test(linear_merge([ (), ((),(),()) ], 
                      [ ((),()),  ((),)*5 ]), 
                      [ (), ((),()), ((),(),()), ((),)*5 ])
 

if __name__ == '__main__':
    main()
