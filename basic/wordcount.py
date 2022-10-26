#!/usr/bin/env python3
    
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# © 2016 Lev Maximov

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Задание wordcount

Функция main() уже реализована и не требует изменения. Она вызывает 
функции print_words() и print_top(), которые необходимо написать вам. 

1. Для запуска с флагом --count реализуйте функцию print_words(filename),
которая подсчитывала бы, как часто слово встречается в тексте, и выводила бы 
на экран результат в таком виде:
word1 count1
word2 count2
...

Список этот должен быть отсортирован по словам в лексикографическом порядке 
(как в словаре). Пунктуация должна быть удалена (если вы не знаете регулярных 
выражений, пунктуацию можно оставить), различия между заглавными и 
строчными делать не надо (то есть «Однако» и «однако» считаются одним и тем 
же словом), слова длиной менее 4 символов нужно игнорировать.

2. Для флага --top реализуйте функцию print_top(filename), которая
делала бы практически то же, что и print_words(filename), но выводила бы только
20 самых часто употребляемых в тексте слов, отсортированных в порядке 
убывания частотности, так что слово, которое чаще всего встречается в тексте, 
шло бы первым, следующее по частоте - вторым и т.д. Слова с одинаковой 
частотностью должны быть отсортированы по алфавиту.

Для обеспечения переиспользования кода (так проще отлаживать, поддерживать), 
выделите часть функций, общую для двух вариантов вызова скрипта, в отдельную 
функцию.

Не пишите всю программу сразу. Разбейте задачу на подзадачи и отлаживайте 
каждую по отдельности (выводите промежуточный результат на экран; когда вы 
добились того, что он соответствует вашим ожиданиям, переходите к следующей 
подзадаче).

"""

import sys
import re
import os
import string

def dict_create(text):
    frequency={}
    match_pattern = re.findall(r'\b[a-zа-я]{4,}\b', text)
    for word in match_pattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1
    return frequency


def print_words(text):
    try:
        with open(text, encoding='utf-8') as f_obj:
            contents = f_obj.read().lower()
    except FileNotFoundError:
        msg = "Sorry, the file " + text + " doesn't exist."
        print(msg)
    else: 
        frequency=dict_create(contents)
        frequency_list = sorted(frequency.keys())
        try:
            os.remove("words.txt")
        except OSError:
            pass
        f1=open("words.txt", 'w', encoding='utf-8')
        for words in frequency_list:
            print(words, frequency[words], file=f1)
    return 

def print_top(text):
    try:
        with open(text, encoding='utf-8') as f_obj:
            contents = f_obj.read().lower()
    except FileNotFoundError:
        msg = "Sorry, the file " + text + " doesn't exist."
        print(msg)
    else: 
        frequency=dict_create(contents)
        frequency_list = list(frequency.items())
        frequency_list.sort(key=lambda item: item[1], reverse=True)
        try:
            os.remove("top_words.txt")
        except OSError:
            pass
        f2=open("top_words.txt", 'w', encoding='utf-8')
        for words in frequency_list[:10]:
            print(words[0], str(words[1]), file=f2)
    return 

# +++your code here+++
# Объявите функции print_words(filename), print_top(filename),
# а также вспомогательную функцию, использующуюся в обеих из них,
# которая принимала бы на вход имя файла и возвращала бы dict.

###

def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --top} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--top':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)

if __name__ == '__main__':
    main()
