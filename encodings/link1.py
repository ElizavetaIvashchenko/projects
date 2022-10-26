import sys
import re
import idna
import os
import string
#Хотя это, наверное, читерский метод :)
def main():
    with open('link1.txt', 'r') as ref:
        for el in ref.readlines():
            print(re.sub(r'//(.*)\b',idna.decode(re.findall(r'//(.*)\b',el)[0]),el))

if __name__ == '__main__':
    main()