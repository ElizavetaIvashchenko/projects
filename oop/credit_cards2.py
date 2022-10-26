#!/usr/bin/env python

# credit_cards2 (необязательная)
#
# Дополнительно нужно проверять и генерировать начальные цифры.
#
# Реализуйте программу для генерирования и проверки валидности
# номеров кредитных карт трёх видов:
#   - visa 13, 16 или 19 цифр, начинается с 4
#   - mastercard 16 цифр, начинается с 51-55 либо с 2221-2720
#   - americanexpress 15 цифр, начинается с 34 либо с 37

import pytest
from random import randint, choice

class CreditCard():

    def __init__(self, number):
        self.num=str(number).replace(' ','') # Сохраняет number в поле класса
        length = 0
        gennum=[]

    def luna_check(self):
        num=[]
        for j in range(len(self.num)):
            num.append(int(self.num[j]))
        luna_sum = 0
        if len(num)%2 == 0:
            for i in range(len(num)):
                if i%2 == 0:
                    num[i]=num[i]*2
                if num[i]>9:
                    num[i]-=9
                luna_sum += num[i]
        else:
            for i in range(len(num)):
                if i%2 == 1:
                    num[i]=num[i]*2
                if num[i]>9:
                    num[i]-=9
                luna_sum += num[i]
        return luna_sum%10==0

    @classmethod
    def generate(cls):
        cls.pregenerate()
        length=cls.length
        fdn=len(cls.gennum)
        num=cls.gennum[:]
        string=''
        check_sum = 0
        if length%2 == 0:
            for i in range(length-1):
                if (i>=fdn):
                    num.append(randint(0,9))
                string+=str(num[i])
                if i%2 == 0:
                    if (num[i]*2<9):
                        check_sum+=num[i]*2
                    else:
                        check_sum+=(num[i]*2-9)
                else:
                    check_sum+=num[i]
        else:
            for i in range(length-1):
                if (i>=fdn):
                    num.append(randint(0,9))
                string+=str(num[i])
                if i%2 == 1:
                    if (num[i]*2<9):
                        check_sum+=num[i]*2
                    else:
                        check_sum+=(num[i]*2-9)
                else:
                    check_sum+=num[i]   
        num.append((10-(check_sum%10))%10)
        string+=str(((10-(check_sum%10))%10))
        return string

class MasterCard(CreditCard):
    @classmethod
    def pregenerate(cls):
        cls.length=16
        if randint(0,1)==0: #0 - 2 знака, 1 - 4 знака
            cls.gennum=[5]
            cls.gennum.append(randint(1,5))
        else:
            cls.gennum=[2]
            rand=str(randint(221,720))
            cls.gennum.extend([int(r) for r in rand])

    def is_valid(self):
        if len(self.num)==16 and self.luna_check() and \
          (int(self.num[0:2]) in range(51,56) or \
           int(self.num[0:4]) in range(2221,2721)):
            return True
        else:
            return False

class Visa(CreditCard):
    @classmethod
    def pregenerate(cls):
        cls.length=choice([13, 16, 19])
        cls.gennum=[4]
        

    def is_valid(self):
        if (len(self.num) in [13,16,19]) and self.luna_check() \
          and int(self.num[0])==4:
            return True
        else:
            return False

class AmericanExpress(CreditCard):
    @classmethod
    def pregenerate(cls):
        cls.length=15
        cls.gennum=choice(([3,4],[3,7]))

    def is_valid(self):
        if len(self.num)==15 and self.luna_check() \
        and int(self.num[0:2]) in [34,37]:
            return True
        else:
            return False

def test0():  assert MasterCard('1223').is_valid() == False
def test1():  assert Visa('1234 5678 9012 3456').is_valid() == False
def test2():  assert Visa('4929 5958 3592 5180').is_valid() == True
def test3():  assert Visa('4929 5958 3592 5181').is_valid() == False
def test4():  assert MasterCard('5578 2350 9610 0287').is_valid() == True
def test5():  assert Visa('5578 2350 9610 0287').is_valid() == False
def test6():  assert AmericanExpress('3473 170111 86210').is_valid() == True
def test7():  assert AmericanExpress('3473 170101 86210').is_valid() == False
def test8():  assert AmericanExpress('3374 170111 86210').is_valid() == False

def test9():
    for i in range(1000):
        n = AmericanExpress.generate()
        assert MasterCard(n).is_valid() == False
        assert AmericanExpress(n).is_valid() == True

if __name__ == '__main__':
    # При таком способе вызова каждый assert вместо просто да/нет будет
    # выдавать более детальную информацию, если что-то пошло не так.
    pytest.main([__file__])
#    pytest.main(['__file__ + '::test3'])    # запускает только третий тест
#    pytest.main(['-s', __file__ + '::test3'])   # то же + возможность отладки ipdb

