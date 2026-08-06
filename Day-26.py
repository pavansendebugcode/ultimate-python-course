# Short hand if else statement it is similar to previous day 10 i will learn but 
# it is write one to two line 
# if else statement

a = 100
b = 200
print('b is large') if (a < b)  else  print('a is large')

'''He can also write here'''

if a<b:
    print('b is large') 
else :                       # similar to above plobem
    print('a is large')


(a == 100)  if a > b  else print('sorry index error')


# Today is also dicuss about the what is enmuerate function
# Enmuerate function are used with loop they also give me index number when loop is work list touple dict.

k = ['abhay', 'anjali', 'chanchel', 'zuned', 'sachin']

# for k in enumerate(k):
# print(k)

# he can also write here you do see the differnt

for index, k in enumerate(k,):
    print(index, k)
    if index == 2:
        print('you are genious')

#for index, k in enumerate(k, start=1):
   # print(index, k)


