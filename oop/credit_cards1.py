#!/usr/bin/env python

# credit_cards1 (обязательная)
#
# Реализуйте программу для генерирования и проверки валидности
# номеров кредитных карт трёх видов:
#   - visa 13, 16 или 19 цифр
#   - mastercard 16 цифр
#   - americanexpress 15 цифр

import pytest
from random import randint, choice

class CreditCard():
    def __init__(self, number):
        self.num=str(number).replace(' ','') # Сохраняет number в поле класса
        self.length=len(self.num)

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
        if luna_sum%10==0:
            return True
        else:
            return False
        return

    @classmethod
    def generate(cls):
        num=[]
        string=''
        check_sum = 0
        length=cls.length
        if length%2 == 0:
            for i in range(length-1):
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
    def is_valid(self):
        if len(self.num)==16 and self.luna_check():
            return True
        else:
            return False
        return 

    @classmethod
    def generate(cls):
        CreditCard.length=16
        return CreditCard.generate()

class Visa(CreditCard):
    def is_valid(self):
        if len(self.num) in [13,16,19] and self.luna_check():
            return True
        else:
            return False
        return

    @classmethod
    def generate(cls):
        CreditCard.length=choice([13,16,19])
        return CreditCard.generate()

class AmericanExpress(CreditCard):
    def is_valid(self):
        print(self.num)
        if len(self.num)==15 and self.luna_check():
            return True
        else:
            return False
        return

    @classmethod
    def generate(cls):
        CreditCard.length=15
        return CreditCard.generate()


def test0():  assert Visa('').is_valid() == False
def test1():  assert MasterCard('1234').is_valid() == False
def test2():  assert Visa('1234 5678 9012 3456').is_valid() == False
def test3():  assert Visa('4929 5958 3592 5180').is_valid() == True
def test4():  assert Visa('4929 5958 3592 5181').is_valid() == False
def test5():  assert MasterCard('5578 2350 9610 0287').is_valid() == True
def test6():  assert AmericanExpress('3473 170111 86210').is_valid() == True
def test7():  assert AmericanExpress('3473 710111 86210').is_valid() == False

def test8():
    # Генерирует номер карты и проверяет его валидность
    for i in range(1000):
        n = Visa.generate()
        assert Visa(n).is_valid() == True
        assert AmericanExpress(n).is_valid() == False

if __name__ == '__main__':
    # При таком способе вызова каждый assert вместо просто да/нет будет
    # выдавать более детальную информацию, если что-то пошло не так.
    pytest.main([__file__])
