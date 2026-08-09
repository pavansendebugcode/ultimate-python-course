''' Map, Filter and Reduce
Map , Filter and Reduce are built in function 
In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and
return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments.'''

## Map

# def cube(x):
#     return x *x*x

l = [1, 2, 3, 5, 4, 6, 5, 8, 9, 6, 6]
# newl = []
# for i in l:
#     newl.append(cube(i))

# print(newl)
# he can also write here this
# newlist = list(map(cube, l))
# print(newlist)

# he can also write here

# newli = list(map(lambda x : x*x*x, l))
# print(newli)

# peroform with touple

# t = (1,2 ,3,4,5,6,7,8,9)
# newt = list(map(lambda x: x*x*x , t))
# print(newt)

## filter

# zuned = filter(cube, l)
# print(list(zuned))

# sachin = filter(lambda x: x>4 , l)
# print(list(sachin))

## ruduce 

# from functools import reduce
# sum = reduce(lambda x, y: x+y, l)

# print(sum)


# todya we are also dicuss about wha is different between is and ==

a = [1, 2, 3, 4 , 5]
b = [1, 2, 3, 4 , 5]

print(a == b) # True
print(a is b) # False

a = "hello"
b = "hello"

print(a == b)  # True
print(a is b)  # True

a = 5
b = 5

print(a == b)  # True
print(a is b)  # True