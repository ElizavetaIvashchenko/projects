import re

# Найдите в тексте слова, содержащие букву ё, и верните список кортежей 
# вида (индекс первой буквы, длина слова).
def yo(text):
    i=0
    tup=[]
    for word in re.findall(r'\w*\b\s*',text):  #это на случай "  "
        if word in re.findall(r'\b\w*[ёЁ]\w*\b\s*',text):
            tup.append(tuple([i, len(re.findall(r'\w*\b',word)[0])]))
        i+=len(word)  
    return tup
# Где-то близко, но вообще, есть метод re.finditer, который возвращает
# прям ровно то, что нужно

# Дан пароль. Проверьте его «сложность»: подсчитайте количество 
# строчных, заглавных букв, цифр, знаков препинания (то есть символов 
# с кодами \x20 до \x1f кроме букв и цифр), а также допустимость, 
# то есть отсутствие символов с кодом меньше 0x20 и больше 0x1f. 
# Верните tuple из 4 чисел и одного bool.
def strength(password):
    a=len(re.findall(r'[a-z]',password))
    A=len(re.findall(r'[A-Z]',password))
    d=len(re.findall(r'\d',password))
    p=len(re.findall(r'[^\w\s]',password))
    if re.findall(r'[^\x20-\x7E]',password):
        return a,A,d,p, False
    else:
        return a,A,d,p, True
#  Лучше так:
#    b = bool(re.findall(r'[^\x20-\x7E]',password)) 
     

# Преобразуйте в строке ссылки в формате MarkDown в html,
# например, [НГУ](http://nsu.ru) -> <a href="http://nsu.ru">НГУ</a>
def markdown(string):
    # names=re.findall(r'\[(\D+?)\]', string)
    # adreses=re.findall(r'\((.*?)\)'  , string)
    return re.sub(r'\[ (\D+?) \]\( (.*?) \)', r'<a href="\2">\1</a>', 
                  string, flags = re.X)
# см. новый тест

# Одним регулярным выражением выделите из списка файлов все, 
# кроме исполняемых (то есть .exe и .bat).
def non_executable(text):
    return re.sub(r'(?: \w|\d )*? (?: \.exe|\.bat )(?= [^a-z\.]|$ )', '', text, 
                  flags=re.X).split()
# вообще, \d входит в \w
# одним это значит совсем одним :) без split.
# Здесь надо использовать look-behind

# Реализуйте функцию sscanf_helper, поддерживающую
# коды %u %d %s %f %e без каких-либо модификаторов, а также код %%,
# которая преобразовывала бы формат sscanf в формат регулярного 
# выражения, например код беззнакового целого '%u' -> '(\d+)'
# %d Any number of decimal digits (0-9), optionally preceded by a sign (+ or -)
# %s Any number of non-whitespace characters, stopping at the first whitespace 
# character found.
# %f A series of decimal digits, optionally containing a decimal point, 
# optionally preceeded by a sign (+ or -) and optionally followed by the e or E
# character and a decimal integer.
# В данном задании в коде %e, в отличие от %f, наличие экспоненты обязательно
# (в C/C++ в обоих кодах экспонента опциональна).
def sscanf_helper(text):
    text=re.sub(r'%u',r'(\d+)',text)
    text=re.sub(r'%d',r'([-+]?\d+)',text)
    text=re.sub(r'%s',r'(\S+)',text)
    text=re.sub(r'%f',r'([-+]?(?: \d+(?:\.\d* )? | \.\d+ ) (?: [eE][-+]? \d+ )?)', text, 0, re.X)
    text=re.sub(r'%e',r'([-+]?(?: \d+(?:\.\d* )? | \.\d+ ) (?: [eE][-+]? \d+ ) )',text, 0, re.X)
    text=re.sub(r'%%',r'\%',text)
    text=re.sub(r' ',r'\s',text)
    return text
# Здесь можно заменять просто replace'ом: так быстрее.
# см. новый тест 

# Напишите функцию sscanf, которая, используя sscanf_helper,
# выполняла бы разбор строки по шаблону и возвращала бы
# найденное в виде tuple.
# Если шаблон не найден – пустой tuple.
def sscanf(s, fmt):
    a=re.search(sscanf_helper(fmt),s)
    return a.groups() if a else ()

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

if __name__ == '__main__':
    print('yo')
    test(yo(''), [])
    test(yo('Ёж'), [(0, 2)])
    test(yo('Четвёртый полёт ещё не завершён.'), 
            [(0, 9), (10, 5), (16, 3), (23, 8)])
    test(yo('Президент Ниинистё живёт в районе Тёёлё в Хельсинки.'), 
            [(10, 8), (19, 5), (34, 5)])

    print()
    print('strength')
    test(strength('qwerty'), (6, 0, 0, 0, True))
    test(strength('Qwerty123!'), (5, 1, 3, 1, True))
    test(strength('Пароль7'), (0, 0, 1, 0, False))
    
    print()
    print('markdown')
    test(markdown('[Google](http://google.com)'), '<a href="http://google.com">Google</a>')
    test(markdown('[1][Google – поиск №1](http://google.com)'), '[1]<a href="http://google.com">Google – поиск №1</a>')
    test(markdown('[Google](http://google.com)(2)'), '<a href="http://google.com">Google</a>(2)')
    test(markdown('[Яндекс!](http://ya.ru) и [百度](http://baidu.com)'), 
                  '<a href="http://ya.ru">Яндекс!</a> и <a href="http://baidu.com">百度</a>')

    print()
    print('non_executable')
    test(non_executable('1.txt dir1 virus.exe 2017-01-02.log'),
         ['1.txt', 'dir1', '2017-01-02.log'])
    test(non_executable('kill_them_all.bat report.doc virus.exe.zip'), 
         ['report.doc', 'virus.exe.zip'])

    print()
    print('sscanf')
    test(sscanf('abc', '%d'), ())
    test(sscanf('10', '%u'), ('10',))
    test(sscanf('10%disk', '%d%%disk'), ('10',))
    test(sscanf('a=-5', '%s=%d'), ('a', '-5'))
    test(sscanf('a=-5%', '%s=%d%%'), ('a', '-5'))
    test(sscanf('a=16%, b=-5', '%s=%u%%, %s=%d'), ('a', '16', 'b', '-5'))
    test(sscanf('/usr/sbin/sendmail - 0 errors, 4 warnings', 
                '%s - %d errors, %d warnings'), 
               ('/usr/sbin/sendmail', '0', '4'))
    test(sscanf('-10, 1.2, .2; 1e-3, -2.3E4', '%d, %f, %f; %f, %f'), 
               ('-10', '1.2', '.2', '1e-3', '-2.3E4'))
