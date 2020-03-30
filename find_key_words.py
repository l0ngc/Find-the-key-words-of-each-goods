import pandas as pd
import numpy as np

#There are three kinds of goods

#define the goods1, goods2, goods3
goods1 = []
goods2 = []
goods3 = []

#find the unique words of each goods
goods1_unique = set()
part = goods1.size() / 10

for j in range(10):
    for i in range(j * part, (j + 1) * part):
        a= set()
        for w in goods1[i].split(' '):
            w_word = ''.join( e for e in w if e.isalnum())
            w_word = w_word.upper()
            a.add(w_word)

    if j == 0:
        goods1_unique = goods1_unique + a
    else:
        goods1_unique = goods1_unique & a

#Then we got the unique words of the goods1
#Then we got the goods2
goods2_unique = set()
part = goods2.size() / 10

for j in range(10):
    for i in range(j * part, (j + 1) * part):
        a= set()
        for w in goods2[i].split(' '):
            w_word = ''.join( e for e in w if e.isalnum())
            w_word = w_word.upper()
            a.add(w_word)

    if j == 0:
        goods2_unique = goods2_unique + a
    else:
        goods2_unique = goods2_unique & a

#Then we got the goods3
goods3_unique = set()
part = goods3.size() / 10

for j in range(10):
    for i in range(j * part, (j + 1) * part):
        a= set()
        for w in goods3[i].split(' '):
            w_word = ''.join( e for e in w if e.isalnum())
            w_word = w_word.upper()
            a.add(w_word)

    if j == 0:
        goods3_unique = goods3_unique + a
    else:
        goods3_unique = goods3_unique & a

#Then we got the intersection of these three goods
inter = goods1_unique & goods1_unique & goods3_unique

#In this way, we can get the key words of each goods
def get_real_words(words_set):
    return words_set - inter
goods1_unique = get_real_words(goods1_unique)
goods2_unique = get_real_words(goods2_unique)
goods3_unique = get_real_words(goods3_unique)

def get_real_words(words_set):
    return words_set - inter


#This might my interesting and this might be one of the first programme that made by my self
#Hello ~~~
#Everything is good and cool~
