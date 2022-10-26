#!/usr/bin/env python3

import re

# Разбейте англ. текст на слова и верните их в виде списка. 
# Апострофы ('), являющиеся частью слова, необходимо оставить, 
# а выступающие в роли кавычек – удалить.
# Никаких иных символов, кроме букв и апострофов, в словах быть не может.
def apostrophe(text):
    # +++your code here+++
    return re.findall(r'\w+[\'\w]*\w*\b',re.sub(r'[^A-Za-z\s\']+','',text))


# Найдите англ. и русские слова, в которые есть три (возможно, разных) 
# гласных подряд и возвратите их в нижнем регистре в виде списка
# в порядке появления в тексте
# Гласными здесь считаются буквы aeuioуеоаыяиюэ
def triple_vowels(text):
    pattern=r'\b\w*[aeuioуеоаыяиюэ]{3}\w*\b'
    return re.findall(pattern,text.lower())
    # Да, верно, хотя [^aeuioуеоаыяиюэ\s]* можно и убрать

# Найдите слова, в которые есть две одинаковые гласных подряд.
# Возвратите отсортированный список без повторов
def double_vowels(text):
    #pattern=r'\b\w*[aeuioуеоаыяиюэ]{2}[^aeuioуеоаыяиюэ\s]*\w*\b' - 2 подряд
    #pattern=r'\b\w*([aeuioуеоаыяиюэ])(\1)\w*\b'
#    return sorted(set(list(word for word in re.findall(r'\b\w*\b', text) \
#                                if re.findall(pattern,word))))
# Всё верно, но лучше так:
    pattern=r'(\w*([aeuioуеоаыяиюэ])\2\w*)'
    return sorted(set(m[0] for m in re.findall(pattern, text)))

# При помощи re.sub найдите в тексте английские слова 
# заканчивающиеся на ly и выделите их при помощи тегов <i> и </i>,
# например "drive carefully" -> "drive <i>carefully</i>"
def mark_adverbs(text):
    return re.sub(r'\w+ly(?=[^a-z]|$)', r'<i>\g<0></i>', text)


# Дана строка.
# При помощи re.sub найдите первое вхождение слов 'не' и 'плох' 
# и eсли 'плох' идет после 'не' замените всю подстроку 'не'...'плох'
# на 'хорош'. # Верните получившуюся строку
# Например, not_bad('Этот ужин не так уж и плох!') вернет:
# 'Этот ужин хорош!'
def not_bad(s):
    # +++ ваш код +++
    return re.sub(r'\bне\s.*?\s*плох(?=[^а-я]|$)','хорош',s,1)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    print('apostrophe')
    test(apostrophe("'It's 5 o'clock already', said he"), 
         ["It's", "o'clock", "already", "said", "he"])
    test(apostrophe("He's bought the 'Best of rock'n'roll' album"), 
        ["He's", 'bought', 'the', 'Best', 'of', "rock'n'roll", 'album'])
    test(apostrophe("I'm sure _I_ shan't be able!"), 
        ["I'm", 'sure', 'I', "shan't", 'be', 'able'])
    test('_'.join(apostrophe(
      """`Perhaps it doesn't understand English,' thought Alice; `I
daresay it's a French mouse, come over with William the
Conqueror.'""")), 
      "Perhaps_it_doesn't_understand_English_thought_Alice_I_daresay_it's_a_"
      "French_mouse_come_over_with_William_the_Conqueror")

    print()
    print('mark_adverbs')
    test(mark_adverbs(
        'Free lyrics web sites are "completely illegal"'),
        'Free lyrics web sites are "<i>completely</i> illegal"')
    test(mark_adverbs('He was replying quickly and angrily'), 
                      'He was replying <i>quickly</i> and <i>angrily</i>')
    test(mark_adverbs('He meticulously called everybody from la to ly in the phonebook'), 
                      'He <i>meticulously</i> called everybody from la to ly in the phonebook')
    test(mark_adverbs('A girl with curly hair walked down the curlyque road.'),
                      'A girl with <i>curly</i> hair walked down the curlyque road.')
    
    print()
    print('triple_vowels')
    test(triple_vowels('He saw a sihlouette of a beautiful queen.'), \
                      ['sihlouette', 'beautiful', 'queen'])
    test(triple_vowels('The ravioli was rather DELICIOUS!!'), ['delicious'])
    test(triple_vowels(u'Жираф - животное длинношеее'), ['длинношеее'])
    test(triple_vowels(u'Бррр, хооолодно!'), ['хооолодно'])

    print()
    print('double_vowels')
    test(double_vowels('А в солнечной Бразилии, Бразилии, Бразилии'),
                      ['Бразилии'])
    test(double_vowels('В Кабардино-Балкарии валокордин из Болгарии'),
                      ['Балкарии', 'Болгарии'])
    test(double_vowels('They found many fishhooks as they stood by the brook.'), \
                      ['brook', 'fishhooks', 'stood'])
    test(double_vowels('Такая стратегия не целесообразна более'), \
                      ['более', 'целесообразна'])

    print()
    print('not_bad')
    test(not_bad('А негр был не плох'), 'А негр был хорош')
    test(not_bad('Да не просто не плох, а совсем не плох'), 'Да хорош, а совсем не плох') 
        # подсказки: аргумент count = количество;
        # если к * добавить ?, это будет означать >=0, но как можно меньше, т.н. nongreedy 

    test(not_bad('Да нет, он был совершенно не плох'), 'Да нет, он был совершенно хорош')
    test(not_bad('Неплохо, совсем не плохо'), 'Неплохо, совсем не плохо')
    test(not_bad('Не очень-то он и сплоховал'), 'Не очень-то он и сплоховал')
    test(not_bad('В стране уголь был, но он был плох'), 'В стране уголь был, но он был плох')
    test(not_bad('Аргумент не плох, да, совсем не плохой аргумент'), 
                 'Аргумент хорош, да, совсем не плохой аргумент')

if __name__ == '__main__':
    main()
