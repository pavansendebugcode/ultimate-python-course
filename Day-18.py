# Hello freind welcome to my python learning journey
#  Today  we are learn what is touple
# Touple is a collection of data item store in single varabile tople is sparted by comma and closed bracket
# The main characterstic of tople is unchangabble after crating touple we cant change

a = (3, 5, 59, 30, 39, 84, 93, 3)
print(type(a), a)

b = ('jaya', 'suhana', 'saloni', 'chunchun')
print(type(b))
print(len(a))

# Touple indexing - are similar to list indexing


'''b = ('jaya', 'suhana', 'saloni', 'chunchun')     positive indexing
        [0]         [1]     [2]         [3]

        
b = ('jaya', 'suhana', 'saloni', 'chunchun')            Negative indexing
     [-4]       [-3]       [-2]      [-1]
'''

print(b[1])
print(a[5])

# check the item in touple 

if 'suhana' in b:
    print("yes")

else:
    print('no')

# Range of indexing

print(a[0:5])
print(b[1:6])
print(a[0: ])
print(a[ : ])

'''Touple are unchangable but nothing is impossible we can do tuple is changable 
    Every person thing how to do they are do but they are possible we are learn how to change touple
    first the touple convert list and modify
    then convert the touple
'''
list = list(a)
list.append(999)
list[2] =  'Mathemites'
print(list)
a =tuple(list)
print(type(a))

# Tuple Method
# 1. count method - count the indivisual number like this

z = a.count(3)
print(z)

# 2. Indexing method- indexing method are use to find index number value present in tuple

y = a.index(999)
print(y)

print(a.short())