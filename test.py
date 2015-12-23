import math
import itertools


b = [[5,1,2,4,1], [1,1,4,1,2]]
c = [1,2,3]
t2 = [['3S', '1D', '1S', 'TC', '4C'],['1H', '5S', '6C', '8C', 'QC']]

#hand_type = [r for r in t2]
#d = [None,3]
#print(max(d))

x = (i*10 for i in range(0,100) if i%7 ==0 )

#a = [first, _, middle, _, last] = [1,2,3,4,5]

#list_shuffle = list(itertools.permutations(a))

def t_yield():
    for iter_range in range(0,10):
        yield iter_range*iter_range

    

#def x_5(x,y):
#    return x+y+5

def square_sum(f, *args):
    return 2*f(*args)

#print(square_sum(x_5,10,5))
#print(len(list_shuffle))

#value_yield = t_yield()
#for i in value_yield:
#    print(i)
#print('first time')

#for i in value_yield:
#    print(i)

t = t_yield()
for i in range(0,5):
    print(next(t))

"""
print(next(x))
print(next(x))
print(next(x))
print('first 3 of x')
for i_g in x:
    print(i_g)
print(x)
for i_g_x in x:
    print(i_g_x)
 """       

a = eval('100==10**2')
print(a)

b = ['a','b']
print(b)
