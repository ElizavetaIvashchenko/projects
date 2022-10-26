import pytest
from itertools import islice, dropwhile, count, zip_longest

# Выполните это же задание через helper-функции из itertools и
# и другие из таблицы по итераторам, не используя yield.

def long_words(iterable, n=4):
    "Возвращает (в виде итератора) слова длиной не менее n символов"
    return filter(lambda x: len(x)>=n, iterable)

def take(iterable, n, fillvalue=None):
    "Первые n элементов в виде списка. Если элементов меньше n,"
    "заполняет оставшееся место значениями fillvalue."
    mylist=list(islice(iterable,0,n))
    if len(mylist) == n:
        return mylist
    else:
        return mylist + [None] * (n-len(mylist))

def tabulate(function, start=0):
    "Возвращает function(0), function(1), ..."
    return map(function, count(start))

def nth(iterable, n, default=None):
    "Возвращает n-й элемент (начиная с 0) либо default"
    return next(islice(iterable,n,None),default)

def dotproduct(vec1, vec2):
    "Вычисляет склярное произведение двух векторов"
    return sum(map(lambda x,y:x*y,vec1,vec2))

def grouper(iterable, n, fillvalue=None):
    "Собирает элементы в группы (tuple'ы) по n элементов. Если в последней"
    "группе недостача, заполняет её при помощи fillvalue"
    tups=[iter(iterable)] * n
    return zip_longest(*tups, fillvalue=fillvalue)

def test0():
    assert list(long_words(
        'Карл клал лук на ларь Клара крала лук с ларя'.split())) == \
        ['Карл', 'клал', 'ларь', 'Клара', 'крала', 'ларя']

def test1():
    assert take([2, 4, 6, 8], 3) == [2, 4, 6]

def test2():
    assert take(tabulate(lambda x: x**2, 5), 3) == [25, 36, 49]

def test3():
    assert nth(tabulate(lambda x: 2*x, 7), 2) == 18

def test4():
    assert dotproduct([1, 2, 3], [2, 3, 4]) == 20

def test5():
    assert list(grouper('ABCDEFG', 3, 'x')) == \
            [('A','B','C'), ('D','E','F'), ('G','x','x')]

if __name__ == '__main__':
    # При таком способе вызова каждый assert вместо просто да/нет будет
    # выдавать более детальную информацию, если что-то пошло не так.
    pytest.main([__file__])
#    pytest.main(['__file__ + '::test3'])    # запускает только третий тест
#    pytest.main(['-s', __file__ + '::test3'])   # то же + возможность отладки ipdb
