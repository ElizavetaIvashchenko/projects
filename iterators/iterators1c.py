import pytest
from itertools import islice, count, zip_longest

# Выполните это же задание через generator-expressions.

# Код получается более компактный и при этом обычно не менее читаемый, 
# чем в предыдущих случаях, правда не все задачи можно решить 
# таким способом.

def long_words(iterable, n=4):
    "Возвращает (в виде итератора) слова длиной не менее n символов."
    return (x for x in iterable if len(x)>=4)

def take(iterable, n, fillvalue=None):
    "Первые n элементов в виде списка. Если элементов меньше n,"
    "заполняет оставшееся место значениями fillvalue."
    "Здесь вместо generator expression нужно использовать list comprehension."
    "list comprehension – это, например, [x**2 for x in range(5)]"
    mylist = list(islice(iterable,0,n))
    if len(mylist) < n:
        mylist+=[fillvalue]*(n-len(mylist))
    return [x for x in mylist] 

def tabulate(function, start=0):
    "Возвращает function(0), function(1), ..."
    return (function(i) for i in count(start))

def dotproduct(vec1, vec2):
    "Вычисляет склярное произведение двух векторов"
    return sum(x*y for x,y in list(zip(vec1,vec2)))

def grouper(iterable, n, fillvalue=None):
    "Собирает элементы в группы (tuple'ы) по n элементов. Если в последней"
    "группе недостача, заполняет её при помощи fillvalue"
    tups=[iter(iterable)] * n
    return (x for x in zip_longest(*tups, fillvalue=fillvalue))


def test0():
    assert list(long_words(
        'Карл клал лук на ларь Клара крала лук с ларя'.split())) == \
        ['Карл', 'клал', 'ларь', 'Клара', 'крала', 'ларя']

def test1():
    assert take([2, 4], 5) == [2, 4, None, None, None]

def test2():
    assert take(tabulate(lambda x: x**2, 5), 3) == [25, 36, 49]

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
