#!/usr/bin/env python

from itertools import islice
import pytest
import matplotlib

# если элемент четный, то следующий a/2
# если элемент нечетный, то следующий 3*a+1

def collatz(n):
    while n != 1:
        #print(n)
        yield n
        n = int(3*n+1) if n%2 else int(n/2)
    if n==1:
        yield n

def it_len(it):
    return sum(1 for i in it)

def test1():
    assert list(collatz(1)) == [1]
    assert list(collatz(4)) == [4, 2, 1]
    assert list(collatz(3)) == [3, 10, 5, 16, 8, 4, 2, 1]
    assert it_len(collatz(75128138247)) == 1229

def vis():
    from matplotlib import pyplot as plt
    a = list(islice(collatz(27), 150))
    print("I am here!")
    plt.plot(a)
    plt.show()

if __name__ == '__main__':
    pytest.main([__file__])
    vis()


