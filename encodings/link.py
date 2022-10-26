import sys
import re
import os
import string

def main():
    with open('link.txt', 'rb') as ref:
        arr=[]
        for el in re.findall(r'%(\w\w)',ref.readlines()[0].decode('utf8')):
        	arr.append(int(el,16))
        print(bytes(arr).decode('utf8'))

if __name__ == '__main__':
    main()