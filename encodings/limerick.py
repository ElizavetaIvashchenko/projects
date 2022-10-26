#!/usr/bin/env python3
"""
Скачайте, распакуйте архив limerick.zip. В нём пять строчек стихотворения.
Каждая записана в своей кодировке, это могут быть такие кодировки как:
'cp1251', 'cp866', 'koi8_r', 'utf8', 'utf_16_be', 'utf_16_le'.

• Прочитайте все строчки в бинарном формате (ключ 'rb' функции open). 

• Определите, какая строка в какой кодировке и раскодируйте (decode) их во 
внутреннее представление.

• Запишите весь стих в файл в кодировке utf8. В качестве разрыва строк 
используйте \n (линуксовые переводы строк) или '\r\n' (виндовые). Файл с 
юниксовыми переводами строк занимает меньше места на диске, но, например, 
notepad их не понимает и записывает весь файл в одну строчку.

• Вычислите контрольную сумму md5 от полученного файла и сравните её 
с limerick-linux.md5 или limerick-windows.md5 в зависимости от того, какой 
символ для разрыва строк вы выбрали.

Контрольная сумма md5 – это последовательность шестнадцатеричных цифр:

>>> from hashlib import md5
>>> md5(b'something').hexdigest()
'437b930db84b8079c2dd804a71936b5f'
"""

import sys
import re
import os
import string

from hashlib import md5

def read_lines():
    lines=[]
    i=0
    names=sorted(os.listdir('./limerick'))
    for name in names:
        with open('./limerick/%s' %name, 'rb') as f:
            string=f.readlines()[0]
            if name=='line1.txt':
                string=string.decode('utf-8')
            if name=='line2.txt':
                string=string.decode('cp866')
            if name=='line3.txt':
                string=string.decode('cp1251')
            if name=='line4.txt':
                string=string.decode('koi8_r')
            if name=='line5.txt':
                string=string.decode('utf_16_be')
            i+=1
            if i!=len(names):
                string+='\n'
            lines.append(string)
    return lines

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
    result = open('result.txt', 'w')
    for line in read_lines():
        result.write(line.encode('utf8').decode('utf8'))
    result.close()

    with open('limerick-linux.md5', 'r') as summ:
        test(md5(open('result.txt', 'rb').read()).hexdigest(),\
             summ.readlines()[0])

if __name__ == '__main__':
    main()
