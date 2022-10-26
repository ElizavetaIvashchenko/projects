#!/usr/bin/env python3
# Измените программу wordcount так, чтобы она обрабатывала не все слова,
# а только имена с отчествами такого вида: Иван Иванович (то есть два слова
# через whitespace, каждое из которых начинается с заглавной буквы).

# При помощи OrderedDefaultDict реализуйте третий ключ --appear, при котором
# имена с отчествами и с частотой употребления выводились бы в порядке появления
# в тексте (appear от order of appearance).

# Файл для тестов - revizor.txt из директории basic.
import sys
import re
import os
import string

from collections import OrderedDict

class OrderedDefaultDict(OrderedDict):
    def __init__(self, default_factory=None, *args, **kwargs):
        OrderedDict.__init__(self, *args, **kwargs)
        self.default_factory = default_factory

    def __missing__(self, key):
        if self.default_factory!=None:
            self[key] = value = self.default_factory()
            return value
        else:
            raise KeyError(key)

    def __repr__(self):
        return 'OrderedDefaultDict(%s, %s' % (self.default_factory,
                                               (OrderedDict.__repr__(self)[19:]))

def dict_create(text):
    frequency = OrderedDefaultDict(int)
    match_pattern = re.findall(r'[А-Я][а-я]+\s[А-Я][а-я]+\b', re.sub(r'\n',' ',text))
# Я бы, конечно, делал замену уже в найденных словах, так значительно быстрее.
# Ну и менять надо не \n а \s: вдруг там двойной пробел встретится или табуляция
# Букву ё за что обидели? ;) В тексте ревизора её случайно не было. Добавил.
    for word in match_pattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1
# Здесь лучше defaultdict(int)
    return frequency


def print_words(text):
    try:
        with open(text, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + text + " doesn't exist."
        print(msg)
    else: 
        frequency=dict_create(contents)
        frequency_list = sorted(frequency.keys())
        try:
            os.remove("count.txt")
        except OSError:
            pass
        f1=open("count.txt", 'w', encoding='utf-8')
        for words in frequency_list:
            print(words, frequency[words], file=f1)
# Записывать в файл тоже лучше через with
    return 

def print_appear(text):
    try:
        with open(text, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + text + " doesn't exist."
        print(msg)
    else: 
        frequency = dict_create(contents)
        frequency_list = frequency.keys()
        try:
            os.remove("appear.txt")
        except OSError:
            pass
        f1=open("appear.txt", 'w', encoding='utf-8')
        for words in frequency_list:
# здесь лучше через .items()
            print(words, frequency[words], file=f1)
    return 

def print_top(text):
    try:
        with open(text, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + text + " doesn't exist."
        print(msg)
    else: 
        frequency=dict_create(contents)
        frequency_list = list(frequency.items())
        frequency_list.sort(key=lambda item: item[1], reverse=True)
# Здесь нужна сортировка по алфавиту при одинаковой частотности
# Как это я не увидел этого, когда вы wordcount сдавали, ума не приложу!
        try:
            os.remove("top.txt")
        except OSError:
            pass
        f2=open("top.txt", 'w', encoding='utf-8')
        for words in frequency_list[:10]:
            print(words[0], str(words[1]), file=f2)
    return 

# +++your code here+++
# Объявите функции print_words(filename), print_top(filename),
# а также вспомогательную функцию, использующуюся в обеих из них,
# которая принимала бы на вход имя файла и возвращала бы dict.

###

def main():
    if len(sys.argv) != 2:
        print('usage: ./revizor.py {--count | --top| --appear} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = 'revizor.txt'
    if option == '--count':
        print_words(filename)
    elif option == '--top':
        print_top(filename)
    elif option == '--appear':
        print_appear(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)

if __name__ == '__main__':
    main()
