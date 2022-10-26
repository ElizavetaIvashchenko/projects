import pytest

# Выполните данное задание при помощи функций-генераторов (то есть
# через yield), без использования модуля itertools и прочих функций из 
# таблицы по итераторам (range использовать можно).

def long_words(iterable, n=4):
    "Возвращает (в виде итератора) слова длиной не менее n символов."
# лучше так:
    for el in iterable:
        if len(el) >= n:
            yield el

# хотя можно, конечно, и так 
def long_words2(iterable, n=4):
    "Возвращает (в виде итератора) слова длиной не менее n символов."
    it = iter(iterable)  # чтобы можно было подавать на вход, например, list
    while True:
        try:
            el = next(it)
            if len(el) >= n:
                yield el
        except:
            break

def take_it(iterator, n, fillvalue=None):
    "Первые n элементов итератора в виде списка. Если в итераторе меньше"
    "n элементов, заполняет оставшееся место значениями fillvalue."
    "Здесь yield не нужен."
    mlist=[]
    i=0
    while i < n:
        try:
            mlist.append(next(iterator))
        except:
            mlist.append(fillvalue)
        i+=1
    return mlist

def take(iterable, n, fillvalue=None):
    "Принимает на вход итерабельный объект: это может быть либо контейнер"
    "(list, dict, и т.д.), либо сразу итератор. Берёт от него итератор"
    "и вызывает take_it от этого итератора."
    it = iter(iterable)
    mylist = list(take_it(it,n,fillvalue))
    return mylist

def tabulate(function, start=0):
    "Возвращает function(0), function(1), ..."
    while True:
        yield function(start)
        start+=1

def nth(iterable, n, default=None):
    "Возвращает n-й элемент (начиная с 0) либо default."
    it=iter(iterable)
    i=0
    while i<=n:
        try:
            el = next(it)
            if (i==n):
                return el
            i+=1
        except:
            return default

def dotproduct(vec1, vec2):
    "Вычисляет склярное произведение двух векторов (yield не нужен)."
    it1=iter(vec1)
    it2=iter(vec2)
    prod=0
    while True:
        try:
            prod+=next(it1)*next(it2)
        except:
            break
    return prod

def grouper(iterable, n, fillvalue=None):
    "Собирает элементы в группы (tuple'ы) по n элементов. Если в последней"
    "группе недостача, заполняет её при помощи fillvalue."
    low=[]
    big=[]
    it=iter(iterable)
    i=0
    while i<n:
        try:
            el = next(it)
            low.append(el)
            i+=1
            if (i==n):
                big.append(tuple(low))
                i=0
                low=[]
        except:
            if (i==1):
                low.append(fillvalue)
                low.append(fillvalue)
                big.append(tuple(low))
                break
            if (i==2):
                low.append(fillvalue)
                big.append(tuple(low))
                break
            break
    return big

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
