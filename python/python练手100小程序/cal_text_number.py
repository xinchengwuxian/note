#coding=utf-8  
import re

with open('d:/my_note/python练手100小程序/english_text.txt', 'r') as f: 
     data = f.read() 

data_split = re.split('[ ,.\n]',data)
data_remove_empty = [i for i in data_split if i  != "" ]
gene = (word for word in data_remove_empty)
for word in gene:
    print(word)
print(len(data_remove_empty))