import pandas as pd
import numpy as np


#import the csv file of each goods

goods1 = pd.read_csv("")
goods2 = pd.read_csv("")
goods3 = pd.read_csv("")

goods1 = goods1['review']
goods2 = goods2['review']
goods3 = goods3['review']

#There are three kinds of goods

#define the goods1, goods2, goods3

#find the unique words of each goods
goods1_unique = set()
part = goods1.size() / 10
#There is no reason that I need 10 groups exactly

for j in range(10):
    for i in range(j * part, (j + 1) * part):
        a= set()
        for w in goods1[i].split(' '):
            w_word = ''.join( e for e in w if e.isalnum())#cut off the other noise
            w_word = w_word.upper()                     #make sure every word is in upper class
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

#In this way, we can get the key words of each goods, some speciallty of each goods
def get_real_words(words_set):
    return words_set - inter

goods1_unique = get_real_words(goods1_unique)
goods2_unique = get_real_words(goods2_unique)
goods3_unique = get_real_words(goods3_unique)

#The we can write each of these into txt files
goods1_file = open("goods1_words", "w")
for i in goods1_unique:
    goods1_file.write(i)
goods1_file.close()

goods_list = ['goods1_unique','goods2_unique','goods3_unique']
files_name = ['goods1_file','goods2_file','goods3_fine']
for i in range(3):
    file_name = files_name[i]
    file_name = open(file_name,'w')
    goods_name = goods_list[i]
    for j in goods_name:
        files_name.write(j)
    file_name.close()


#This might my interesting and this might be one of the first programme that made by my self
#Hello ~~~
#Everything is good and cool~
    