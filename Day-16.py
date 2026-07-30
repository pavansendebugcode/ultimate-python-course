# Today we discuss what is list 
# * List is use for to store multiple in one varabile 
# * List are enclosed by square bracket like this []
# * List are the changable after creation

# Example

list_marks = [5, 6, 8, 20, 40, 100 , 5000, 989, 9999]
print(list_marks)

list_myfriends = ["Abhay", "Nikhil", "Sachin", "Zunead", ]
print(list_myfriends)

list_mygoal = [1, 4, 3, 'i want to become a rich man']
print(list_mygoal)

# list indexing

# 1. Postive indexing 
# 2. Negative indexing

'''list_myfriend = ["Abhay", "Nikhil", "Sachin", "Zunead", ]
                        [0]     [1]     [2]         [3]

list_myfriends = ["Abhay", "Nikhil", "Sachin", "Zunead", ]
                    [-4]     [-3]      [-2]       [-1]

'''

# Access element by using indexing

a = list_myfriends[0]
b = list_myfriends[1]
c = list_myfriends[2]
print(a)
print(b)
print(c)


d = list_myfriends[-1]
e = list_myfriends[-2]
f = list_myfriends[-3]
print(d)
print(e)
print(f)

# check element present in list 
 
if 5 in list_marks:
    print('yes')

else :
    print('No')


# Range of indexing
# Access element to the list by using indexing

print(list_marks[1:4]) # Postive indexing
print(list_marks[-5:-1]) # Negative indexing

print(list_marks[0: ])
print(list_marks[ : -1])
print(list_marks[0:6:2])


# Access indivisual word in present in string in the list

myfriends = ["Abhay", "Nikhil", "Sachin", "Zunead", ]
p = [item for item in myfriends if 'a' in item]
print(p)
