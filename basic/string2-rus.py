#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# Перевод, дополнения Максимов Л.В. © 2016

# Дополнительные упражнения на строки

# E. Суффиксы
# Если длина строки на входе составляет 3 или более символов,
# добавьте к строке окончание 'ing', если только она уже
# не заканчивается на 'ing', в случае чего добавьте к ней
# суффикс 'ly'.
# Если же длина входной строки менее трех символов, 
# верните её в неизменном виде
def verbing(s):
    if len(s)>=3:
        if s[-3:] != 'ing':
            return s + 'ing'
        else:
            return s + 'ly'
    else:
        return s
    return
 
# F. Хорош
# Дана строка.
# Найдите первое вхождение подстрок 'не' и 'плох'.
# Если 'плох' идет после 'не' - замените всю подстроку
# 'не'...'плох' на 'хорош'.
# Верните получившуюся строку
# Например, 'Этот ужин не так уж плох!' вернет:
# 'Этот ужин хорош!'
def not_bad(s):
    start=s.find('не')
    end=s.find('плох')
    if end!=(-1) and end>start: 
        return s[0:start]+'хорош'+s[(end+len('плох')):]
    else:
        return s
 
# G. Две половины
# Определим следующий способ разделения строки на две половины:
# Если длина четная - обе половины имеют одинаковую длину.
# Если длина нечетная — дополнительный символ присоединяется к первой половине.
# Таким образом, у строки 'abcde' первая половина - 'abc', вторая - 'de'.
# Даны 2 строки: a и b, верните строку вида:
# 1-половина-a + 1-половина-b + 2-половина-a + 2-половина-b
def front_back(a, b):
    if (len(a)%2)!=0:
        first_half_a=a[:((len(a)//2)+1)]
        second_half_a=a[((len(a)//2)+1):]
    else:
        first_half_a=a[:(len(a)//2)]
        second_half_a=a[(len(a)//2):]
    if (len(b)%2)!=0:
        first_half_b=b[:((len(b)//2)+1)]
        second_half_b=b[((len(b)//2)+1):]
    else:
        first_half_b=b[:(len(b)//2)]
        second_half_b=b[(len(b)//2):]
    return first_half_a+first_half_b+second_half_a+second_half_b
 
# H. Яблоки
def apples(n):
    words = ["яблоко", "яблока", "яблок"]
    inumber = n % 100
    if inumber >= 11 and inumber <=19:
        words = words[2]
    else:
        iinumber = inumber % 10 
        if iinumber == 1:
            words = words[0]
        elif iinumber == 2 or iinumber == 3 or iinumber == 4:
            words = words[1]
        else:
            words = words[2]
    return 'На столе %s' %(n)+' ' +words
    

 
# Простая функция test() используется в main() для сравнения того, 
# что возвращает с функция с тем, что она должна возвращать.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s | Ожидалось: %s' % (prefix, repr(got), repr(expected)))
 
 
# Вызывает определённые выше функции с тестовыми параметрами.
def main():
    print('Суффиксы')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('Хорош')
    test(not_bad('Этот фильм не так уж плох'), 'Этот фильм хорош')
    test(not_bad('А ужин был неплох, совсем не плох!'), 'А ужин был хорош, совсем не плох!')
    test(not_bad('Этот чай уже не горячий'), 'Этот чай уже не горячий')
    test(not_bad('Этот плох, но не совсем'), 'Этот плох, но не совсем')
 
    print()
    print('Две половины')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('абвгде', 'ЭЮЯ'), 'абвЭЮгдеЯ')
    test(front_back('Дон', 'Кихот'), 'ДоКихнот')
 
    print()
    print('Яблоки')
    test(apples(14), 'На столе 14 яблок')
    test(apples(22), 'На столе 22 яблока')
    test(apples(50), 'На столе 50 яблок')
    test(apples(101), 'На столе 101 яблоко')
    test(apples(112), 'На столе 112 яблок')
    for i in range(300):
        if i%100 <= 26:
            print(apples(i))
 
# Стандартный шаблон для вызова функции main().
if __name__ == '__main__':
    main()
