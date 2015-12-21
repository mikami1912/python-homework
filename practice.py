"""
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print ','.join(l)


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x = int(raw_input())
print fact(x)

import math

dict_number = {}
input_number = int(raw_input("Input your #:"))

for i in range(1, input_number+1):
    dict_number[i] = i*i

print(dict_number)


class input_String():
    def __init__(self):
        self.value = ""
    
    def getString(self):
        self.value = raw_input("Nhap 1 tu:")    
        return self.value
    
    def printString(self):
        print(self.value.upper())
        
a = input_String()
b = a.getString()
a.printString()

import math
list_number = []
input_number = raw_input("Nhap 1 day so, cach bang ',' :")

list_number = input_number.split(',')
result = []

for i in list_number:
    i = int(i)
    result.append(math.sqrt((2*50*i)/30))

print(result)


row_index = 7
col_index = 4
list_number = [[0 for col in range(col_index)] for row in range(row_index)]

print(list_number)
for index_i in range(0,row_index):
    print '\n'
    for index_j in range(0,col_index):
        list_number[index_i][index_j] = index_i*index_j
        print index_i,'*',index_j,' = ',list_number[index_i][index_j]
        
        
raw_input()


input_string = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
normalize_word = input_string.split(' ')
list_word = []
dict_word = {}
for word in normalize_word:
    if word not in list_word:
        list_word.append(word)
        dict_word[word] = 1
    else: dict_word[word] += 1

print dict_word
"""
x = '5' + 'D'

print x 



 
    
    
    
        
    


